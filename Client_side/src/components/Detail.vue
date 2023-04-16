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
                    <el-breadcrumb-item><a href="#">查看详情</a></el-breadcrumb-item>
                </el-breadcrumb>
                <el-col :span="9">
                    <el-card class="imgShow" :body-style="{ padding: '0px'}">
                    <img src="../assets/adult-4402808_640.jpg" class="image">
                    </el-card>
                    <el-card class="patientInfo">
                        <el-descriptions title="患者信息" :column=2>
                            <el-descriptions-item label="姓名">{{ patientInfo.patient_name }}</el-descriptions-item>
                            <el-descriptions-item label="性别">{{ patientInfo.gender }}</el-descriptions-item>
                            <el-descriptions-item label="年龄">{{ patientInfo.age }}</el-descriptions-item>
                            <el-descriptions-item label="民族">{{ patientInfo.nation }}</el-descriptions-item>
                        </el-descriptions>
                        <el-descriptions :column=1>
                            <el-descriptions-item label="身份证号">{{ patientInfo.card }}</el-descriptions-item>
                            <el-descriptions-item label="联系电话">{{ patientInfo.phone }}</el-descriptions-item>
                            <el-descriptions-item label="邮箱">{{ patientInfo.email }}</el-descriptions-item>
                            <el-descriptions-item label="住址">{{ patientInfo.address }}</el-descriptions-item>
                        </el-descriptions>
                    </el-card>
                </el-col>
                <el-col span="15">
                    <el-card class="patientInfo">
                        <el-descriptions title="患者病情" :column=1>
                            <el-descriptions-item label="主诉">{{ form2.chief_complaint }}</el-descriptions-item>
                            <el-descriptions-item label="既往病史">{{ form2.medical_history }}</el-descriptions-item>
                            <el-descriptions-item label="诊断结果">{{ form2.diagnosis_result }}</el-descriptions-item>
                            <el-descriptions-item label="医嘱">{{ form2.proposals }}</el-descriptions-item>
                        </el-descriptions>
                        <el-col span="11">
                            <img :src="image" alt="" style="width:90%; height: 90%; margin: 30px 0;">
                        </el-col>
                        <el-col span="2"></el-col>
                        <el-col span="11">
                            <img :src="image2" alt="" style="width:90%; height: 90%; margin: 30px 0;">
                        </el-col>
                    </el-card>
                </el-col>
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

    .main .imgShow {
        background: #fff;
        border-radius: 10px;
        height: 244px;
        margin: 10px 20px;
    }

    .patientInfo {
        background: #fff;
        border-radius: 10px;
        margin: 10px 20px;
    }

    .patientInfo >>> .el-descriptions__title {
        color: #409eff;
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
                patientInfo: '',
                form2: '',
                image: '',
                image2: '',
            }
        },
        computed: {
        ...mapState({
                userInfo: state => state.user,
            })
        },
        methods: {
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
                that.patientInfo = data.info;
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

            // 获取图像
            this.$axios.post('image/read/',
                this.$qs.stringify({
                'id': that.$route.params.id
                })
            ).then(function (res) {
                    let data = res.data;
                    if(data.code === 200) {
                        that.image = 'data:image/jpeg;base64,' + data.img_data;
                        that.image2 = 'data:image/jpeg;base64,' + data.img_data2;
                    } else {
                        that.$message.error(data.msg);
                    }
            }).catch(function (err) {
                console.log(err);
                that.$message.error('获取图像信息失败');
            });
        }
    };
</script>