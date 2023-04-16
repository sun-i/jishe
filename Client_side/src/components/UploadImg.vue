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
            <el-menu router default-active="/AIassistance" class="el-menu-vertical-demo"  active-text-color="#66b1ff" :default-openeds="['1']">
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
                    <el-breadcrumb-item><a href="#">AI辅助诊断</a></el-breadcrumb-item>
                </el-breadcrumb>
                <el-card class="image" v-loading="loading">
                    <el-row style="height: 300px;">
                        <el-col span=5></el-col>
                        <el-col span=7>
                            <div style="margin-top: 140px;">
                                <el-button type="primary" @click="chosePatient" v-if="!is_success">上传图像</el-button>
                                <el-button type="success" v-if="is_success">上传成功</el-button>
                            </div>
                        </el-col>
                        <el-col span=7>
                            <template >
                                <el-skeleton style="width: 240px; margin-top: 30px" v-if="!is_success">
                                    <template slot="template">
                                    <el-skeleton-item variant="image" style="width: 240px; height: 240px;" />
                                    </template>
                                </el-skeleton>
                            </template>
                            <img :src="image" alt="" style="width:100%; height:100%" v-if="is_success">
                        </el-col>
                        <el-col span=5></el-col>
                    </el-row>
                    <el-button type="primary" @click="goto" style="margin-top:20px">一键检测</el-button>
                </el-card>
                
                

                <el-dialog title="选择患者" :visible.sync="doctorDialogTableVisible" width="70%">
                    <el-table
                    :data="patientInfo"
                    class="recordTable">
                    <el-table-column
                    label="预约编号"
                    width="80px" type="index">
                    </el-table-column>
                    <el-table-column
                    label="病人姓名"
                    prop="patient_name" width="100px">
                    </el-table-column>
                    <el-table-column
                    label="联系方式"
                    prop="phone" width="127px">
                    </el-table-column>
                    <el-table-column
                    label="邮箱"
                    prop="email" width="127px">
                    </el-table-column>
                    <el-table-column
                    label="状态"
                    width="140px">
                            <template slot-scope="scope">
                                <el-tag type="warning" v-if="scope.row.isFinished === 0">待检测中</el-tag>
                                <el-tag type="success" v-else>检测完成</el-tag>
                            </template>
                    </el-table-column>
                    <el-table-column
                    align="right" width="150px">
                    <template slot-scope="scope">
                            <el-button @click="readPatientImage(scope.row.id)" type="text"
                                                       size="small">选择
                            </el-button>
                    </template>
                    </el-table-column>

                </el-table>
                            </el-dialog>

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

    .image {
        margin: 20px;
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
        height: 400px;
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
                patientInfo:'',
                active:1,
                doctorDialogTableVisible: false,
                searchData: '',
                image: '',
                is_success: false,
                loading: false,
            }
        },
        computed: {
        ...mapState({
                userInfo: state => state.user,
            }),
        },
        methods: {
            chosePatient() {
                this.doctorDialogTableVisible = true;
            },

            readPatientImage(id) {
            let that = this;
            this.$axios.post('image/read/',
                this.$qs.stringify({
                'id': id
                })
            ).then(function (res) {
                    let data = res.data;
                    if(data.code === 200) {
                        that.doctorDialogTableVisible = false;
                        that.is_success = true;
                        that.image = 'data:image/jpeg;base64,' + data.img_data;
                        window.localStorage.setItem('img_path', data.img_path);
                        window.localStorage.setItem('img_data1', data.img_data);
                        window.localStorage.setItem('record_id', id);
                    } else {
                        that.$message.error(data.msg);
                    }
            }).catch(function (err) {
                console.log(err);
                that.$message.error('获取图像信息失败');
            });
            },

            goto() {
                this.loading = true;
                let that = this;
                this.$axios.post('detection/load/',
                this.$qs.stringify({
                'img_path': window.localStorage.getItem('img_path')
                    })
                ).then(function (res) {
                        let data = res.data;
                        if(data.code === 200) {
                            window.localStorage.setItem('prob', data.prob);
                            window.localStorage.setItem('img_data2', data.data);
                            that.loading = false;
                            that.$router.push('/report');
                        } else {
                            that.$message.error(data.msg);
                        }
                }).catch(function (err) {
                    console.log(err);
                    that.$message.error('检测失败');
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
            let that = this
            let url = '/patient/uncheck/' + this.$store.state.user.id
            this.$axios.get(url).then(function (data) {
                data = data.data;
                that.patientInfo = data.list;
            }).catch(function (err) {
                console.log(err);
                that.$message.error('获取挂号记录失败');
            });
        }
    };
</script>