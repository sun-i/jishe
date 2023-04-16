<template>
    <el-container>
        <el-header class="head">
                <h3>肿瘤Xpert</h3>
                <el-input placeholder="请输入内容" class="input-with-select" size="small" v-model="input1">
                    <el-button slot="append" icon="el-icon-search" size="small"></el-button>
                </el-input>
                <el-link class="el-icon-s-tools" :underline="false"></el-link>
                <el-link class="el-icon-switch-button" :underline="false" @click="out"></el-link>
                <el-link class="el-icon-message-solid" :underline="false"></el-link>
        </el-header>
        <el-container> 
            <el-aside width="200px" class="aside">
            <div class="block"><el-avatar :size="50" :src="circleUrl"></el-avatar></div>
            <div class="username">{{ userInfo.name !== '' ? userInfo.name : '张 三'}}</div>
            <div class="infoIcon">
                <el-link class="el-icon-message" :underline="false"></el-link>
                <el-link class="el-icon-collection" :underline="false"></el-link>
                <el-link class="el-icon-data-line" :underline="false"></el-link>
                <el-link class="el-icon-date" :underline="false"></el-link>
            </div>
            <el-divider></el-divider>
            <el-menu router default-active="/recordManage" class="el-menu-vertical-demo"  active-text-color="#66b1ff" :default-openeds="['1']">
            <el-submenu class="patientManage" index="1">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>患者管理</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item index="/appointManage">预约管理</el-menu-item>
                    <el-menu-item index="/recordManage">挂号管理</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="/AIassistance">
                <i class="el-icon-coordinate"></i>
                <span slot="title">AI辅助诊断</span>
            </el-menu-item>
            </el-menu>
        </el-aside>
            <el-main class="main">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/patientIndex' }">医生</el-breadcrumb-item>
                    <el-breadcrumb-item><a href="#">患者管理</a></el-breadcrumb-item>
                    <el-breadcrumb-item><a href="#">挂号管理</a></el-breadcrumb-item>
                    <el-breadcrumb-item><a href="#">撰写病历</a></el-breadcrumb-item>
                </el-breadcrumb>
                <el-card class="record">
                    <h4 style="text-align: left; color:#409eff; margin-bottom: 30px;"><i class="el-icon-document"></i>&nbsp;&nbsp;患者信息</h4>
                    <el-form ref="form1" :model="form1" label-width="40px" :disabled=true label-position="left">
                        <el-row>
                            <el-col :span="8">
                                <el-form-item label="姓名">
                                    <el-input v-model="form1.name"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="3"></el-col>
                            <el-col :span="8">
                                <el-form-item label="性别">
                                    <el-select v-model="form1.gender" placeholder="性别">
                                        <el-option label="男" value="男"></el-option>
                                        <el-option label="女" value="女"></el-option>
                                    </el-select>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="8">
                                <el-form-item label="民族">
                                    <el-input v-model="form1.nation"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="3"></el-col>
                            <el-col :span="8">
                                <el-form-item label="年龄">
                                    <el-input v-model="form1.age"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="19">
                                <el-form-item label="证件">
                                    <el-input v-model="form1.card"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="8">
                                <el-form-item label="电话">
                                    <el-input v-model="form1.phone"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="3"></el-col>
                            <el-col :span="8">
                                <el-form-item label="邮箱">
                                    <el-input v-model="form1.email"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="19">
                                <el-form-item label="住址">
                                    <el-input v-model="form1.address"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                    </el-form>
                    <el-divider></el-divider>
                    <h4 style="text-align: left; color:#409eff; margin: 30px 0;"><i class="el-icon-document"></i>&nbsp;&nbsp;我的医嘱</h4>
                    <el-form ref="form2" :model="form2" label-width="70px" label-position="left">
                        <el-row>
                            <el-col :span="8">
                                <el-form-item label="就诊号">
                                    <el-input v-model="form2.id"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="3"></el-col>
                            <el-col :span="8">
                                <el-form-item label="就诊科室">
                                    <el-input v-model="form2.clinic"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-form-item label="主诉">
                            <el-input type="textarea" v-model="form2.chief_complaint"></el-input>
                        </el-form-item>
                        <el-form-item label="既往病史">
                            <el-input type="textarea" v-model="form2.medical_history"></el-input>
                        </el-form-item>
                        <el-form-item label="诊断结果">
                            <el-input type="textarea" v-model="form2.diagnosis_result"></el-input>
                        </el-form-item>
                        <el-form-item label="医嘱">
                            <el-input type="textarea" v-model="form2.proposals"></el-input>
                        </el-form-item>
                        <el-button type="primary" @click="save">提交</el-button>
                    </el-form>
                
                </el-card>
            </el-main>
        </el-container>
    </el-container>
</template>
  
<style scoped>
    h3 {
        margin: 17px 30px;
        float: left;
    }

    .input-with-select {
        float: left;
        width: 300px;
        margin: 15px 50px;
    }

    .head {
        background: #fff;
    }

    .aside {
        padding-bottom: 300px;
        background: #fff;
    }

    .head .el-link {
        float: right;
        margin: 22px 20px;
        font-size: 18px;
    }

    .el-avatar {
        margin: 30px 0 5px 0;
        box-shadow: 0 0 5px #cac6c6;
        border-radius: 50%;
        border: 2px solid #fff;
    }

    .username {
        text-align: center;
        font-size: 16px;
        font-weight: 550;
        color: #505458;
        font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    }

    .infoIcon {
        margin: 20px 0 0 0;
    }

    .infoIcon .el-link {
        margin: 0 7px;
        font-size: 18px;
    }

    .el-divider--horizontal {
        margin: 24px 0 5px 0;
    }

    .el-aside .el-menu .el-menu-item {
        font-size: 14px;
        font-weight: 540;
        color: #909399;
        border: none;
    }

    .el-aside .el-menu {
        border: none;
    }

    .main {
        background-color: #f4f6fa;
        box-shadow: inset 0px 0px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        padding: 20px;
    }

    .main .el-breadcrumb {
        padding: 20px;
        margin: 20px;
        background-color: #fff;
        border-radius: 10px;
    }

    .record {
        margin: 20px;
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
    }
    .el-col {
        border: 1px solid transparent;
    }

</style>
  
<script>
    import { mapState } from 'vuex'
    export default {
        name: 'patientRecord',
        data() {
            return {
                input1: '',
                circleUrl: "https://img.imgdd.com/f210f3.55703645-a467-4fea-b91c-40c74bd30aad.png",
                form1: {
                    name: '',
                    age: '',
                    email: '',
                    phone: '',
                    address: '',
                    nation: '',
                    card: '',
                    gender: '',
                },
                form2: {
                    id: '',
                    clinic: '',
                    chief_complaint: '',
                    medical_history:' ',
                    proposals:'',
                    diagnosis_result:''
                }
            }
        },
        computed: {
        ...mapState({
                userInfo: state => state.user,
            })
        },
        methods: {
            save() {
                let that = this;
                this.$axios.post('detection/medicword/', this.$qs.stringify(
                    {
                        recordId: this.$route.params.id,
                        a1: this.form2.id,
                        a2: that.form2.clinic,
                        a3: that.form2.chief_complaint,
                        a4: that.form2.medical_history,
                        a5: that.form2.proposals,
                        a6: that.form2.diagnosis_result
                    }
                )).then(function (data) {
                    data = data.data;
                    if(data.code === 200) {
                        that.$message.success('保存成功');
                    } else {
                        that.$message.error(data.msg);
                    }
                }).catch(function (err) {
                    console.log(err);
                    that.$message.error('保存失败');
                });
            },
            out() {
                this.$confirm('是否退出登录?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                    localStorage.clear();
                    window.location.reload();
                    this.$message({
                        type: 'success',
                        message: '退出登录成功!'
                    });
                }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消'
                });          
                });
            }
        },

        mounted() {
            let that = this;
            // 获取患者信息
            this.$axios.get('patient/' + that.$route.params.id + '/').then(function (data) {
                data = data.data;
                that.form1 = data.info;
            }).catch(function (err) {
                that.$message.error('获取患者信息失败');
            });

            // 获取门诊信息
            this.$axios.get('medic/' + that.$route.params.id + '/').then(function (data) {
                data = data.data;
                if(data.code === 200) {
                    that.form2 = data;
            } else {
                that.$message.error(data.msg);
            }
            }).catch(function (err) {
                console.log(err);
                that.$message.error('获取病历信息失败');
            });
        }
    };
</script>