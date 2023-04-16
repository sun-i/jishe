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
            <el-menu router default-active="" class="el-menu-vertical-demo" active-text-color="#66b1ff">
                <el-menu-item index="/appointment">
                    <i class="el-icon-s-data"></i>
                    <span slot="title">预约诊断</span>
                </el-menu-item>
                <el-menu-item index="/patientRecord">
                    <i class="el-icon-menu"></i>
                    <span slot="title">挂号记录</span>
                </el-menu-item>
            </el-menu>
        </el-aside>
            <el-main class="main">
                <el-card shadow="always" class="main_head">
                    <div class="head_bg">
                        <div class="block"><el-avatar :size="50" :src="circleUrl"></el-avatar></div>
                        <div class="name">
                            <div>
                                <div style="font-size: 13px; font-weight: bolder; color: #66b1ff;">{{ userInfo.name !== '' ? userInfo.name : '张 三'}}</div>
                                <div>name</div>
                            </div>
                            <div>
                                <div style="font-size: 13px; font-weight: bolder; color: black;">{{ userInfo.email !== '' ? userInfo.email : '123@email.com'}}</div>
                                <div>E-mail</div>
                            </div>
                        </div>
                    </div>
                </el-card>
                <el-col :span="8">
                    <el-card shadow="always" class="fans">
                        <div class="data">
                            <ul>
                                <li>
                                    <span>
                                        <span class="li-hint-top">852</span>
                                        <span class="li-hint">关注</span>
                                    </span>
                                                    </li>
                                                    <li>
                                    <span>
                                        <span class="li-hint-top">13k</span>
                                        <span class="li-hint">粉丝</span>
                                    </span>
                                                    </li>
                                                    <li>
                                    <span>
                                        <span class="li-hint-top">234</span>
                                        <span class="li-hint">私信</span>
                                    </span>
                                </li>
                            </ul>
                        </div>
                        <div style="margin-top: 10px;">
                            <el-button type="primary" round>粉丝</el-button>
                            <el-button type="primary" round>信箱</el-button>
                        </div>
                    </el-card>
                    <el-card class="timeline">
                        <el-timeline>
                            <el-timeline-item
                            v-for="(activity, index) in activities"
                            :key="index"
                            :icon="activity.icon"
                            :type="activity.type"
                            :color="activity.color"
                            :size="activity.size"
                            :timestamp="activity.timestamp">
                            {{activity.content}}
                            </el-timeline-item>
                        </el-timeline>
                    </el-card>
                </el-col>
                <el-card class="userInfo" style="height: 495px;">
                    <el-col>
                    <el-tabs v-model="activeName">
                        <el-tab-pane label="个人信息" name="first" style="width: 100%;" >
                            <el-form ref="form" :model="form" label-width="40px" :disabled=isButtonClicked>
                                <el-row>
                                    <el-col :span="8">
                                        <el-form-item label="姓名">
                                            <el-input v-model="form.name"></el-input>
                                        </el-form-item>
                                    </el-col>
                                    <el-col :span="3"></el-col>
                                    <el-col :span="8">
                                        <el-form-item label="性别">
                                            <el-select v-model="form.gender" placeholder="性别">
                                                <el-option label="男" value="男"></el-option>
                                                <el-option label="女" value="女"></el-option>
                                            </el-select>
                                        </el-form-item>
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="8">
                                        <el-form-item label="民族">
                                            <el-input v-model="form.nation"></el-input>
                                        </el-form-item>
                                    </el-col>
                                    <el-col :span="3"></el-col>
                                    <el-col :span="8">
                                        <el-form-item label="年龄">
                                            <el-input v-model="form.age"></el-input>
                                        </el-form-item>
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="19">
                                        <el-form-item label="证件">
                                            <el-input v-model="form.card"></el-input>
                                        </el-form-item>
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="8">
                                        <el-form-item label="电话">
                                            <el-input v-model="form.phone"></el-input>
                                        </el-form-item>
                                    </el-col>
                                    <el-col :span="3"></el-col>
                                    <el-col :span="8">
                                        <el-form-item label="邮箱">
                                            <el-input v-model="form.email"></el-input>
                                        </el-form-item>
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="19">
                                        <el-form-item label="住址">
                                            <el-input v-model="form.address"></el-input>
                                        </el-form-item>
                                    </el-col>
                                </el-row>
                            </el-form>
                            <el-row>
                                    <el-col :span="19">
                                        <el-button  v-show="isButtonClicked" type="primary" @click="modifyInfo">修改信息</el-button>
                                        <el-button v-show="!isButtonClicked" type="primary" @click="saveInfo">保存信息</el-button>
                                        <el-button v-show="!isButtonClicked" @click="cancel">取消</el-button>
                                    </el-col>
                                </el-row>
                        </el-tab-pane>
                        <el-tab-pane label="认证配置" name="second">认证配置</el-tab-pane>
                        <el-tab-pane label="更多设置" name="third">更多设置</el-tab-pane>
                    </el-tabs>
                </el-col>
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

    .main_head {
        background: #fff;
        border-radius: 10px;
        height: 230px;
        margin: 10px 20px;
    }
    .main_head .head_bg{
        position: relative;
        display: block;
        background: url("https://img.imgdd.com/f210f3.3c7a7196-b197-41e8-82bc-b7348fc46ae1.png") no-repeat;
        border-radius: 10px;
        background-size: cover;
        width: 100%;
        height: 150px;
    }

    .head_bg .block {
        position: absolute;
        bottom: -35px;
        left: 15px;
    }

    .head_bg .name {
        position: absolute;
        bottom: -38px;
        left: 34px;
        font-size: 8px;
        font-weight: normal;
        color:#909399;
        font-family: poppins;
    }

    .head_bg .name > div {
        float: left;
        margin: 0 50px;
    }

    .fans {
        background: #fff;
        border-radius: 10px;
        height: 100%;
        margin: 10px 20px;
    }

    .data ul > li {
        display: inline-block;
        width: 20%;
        height: 100%;
        margin-left: 6%;
        margin-right: 6%;
    }

    .li-hint, .li-hint-top {
        width: 100%;
        height: 20px;
        /*background-color: rgba(250, 250, 210, 0.5);*/
        display: block;
        margin-top: 10px;
        font-size: 12px;
        font-family: poppins;
        color: #969BA0;
    }

    .li-hint-top {
        font-size: 20px;
        color: black;
        font-weight: 600;
    }

    .timeline {
        background: #fff;
        border-radius: 10px;
        height: 100%;
        margin: 10px 20px;
    }

    .timeline >>> .el-timeline-item__wrapper {
        font-family: poppins;
        text-align: left;
    }

    .userInfo {
        background: #fff;
        border-radius: 10px;
        height: 100%;
        margin: 20px 20px;
    }

    .userInfo >>> .el-tabs__nav-wrap::after{
        height: 0;
    }
    .el-col {
        border: 1px solid transparent;
    }

</style>
  
<script>
    import { mapState } from 'vuex'
    export default {
        name: 'PatientIndex',
        data() {
            return {
                activeName: 'first',
                input1: '',
                circleUrl: "https://img.imgdd.com/f210f3.55703645-a467-4fea-b91c-40c74bd30aad.png",
                activities: [{
                    content: '完成下载病历单',
                    timestamp: '2023-04-12 20:46',
                    }, {
                    content: '完成首次确诊',
                    timestamp: '2023-04-04 20:46',
                    color: '#0bbd87'
                    }, {
                    content: '完成首次预约',
                    timestamp: '2023-04-03 21:46',
                    color: '#66b1ff'
                    }, {
                    content: '完成实名认证',
                    timestamp: '2023-04-03 21:00',
                    color: '#66b1ff'
                    }, {
                    content: '完成注册',
                    timestamp: '2023-04-03 20:46',
                    color: '#66b1ff'
                }],
                form: {
                    name: this.$store.state.user.name,
                    age: this.$store.state.user.age,
                    email: this.$store.state.user.email,
                    phone: this.$store.state.user.phone,
                    address: this.$store.state.user.address,
                    nation: this.$store.state.user.nation,
                    card: this.$store.state.user.card,
                    gender: this.$store.state.user.gender
                },
                isButtonClicked: true,
            }
        },
        computed: {
        ...mapState({
                userInfo: state => state.user,
            })
        },
        methods: {
            modifyInfo() {
                this.isButtonClicked = false;
            },
            saveInfo() {
                console.log(this.$store.state.user.username);
                this.$axios
                    .post('user/patient/modify/', this.$qs.stringify({
                        id: this.$store.state.user.id,
                        name: this.form.name,
                        age: this.form.age,
                        email: this.form.email,
                        phone: this.form.phone,
                        address: this.form.address,
                        nation: this.form.nation,
                        card: this.form.card,
                        gender: this.form.gender
                    }), {// 发送表单格式数据
                        headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                        }
                    })
                    .then(successResponse => {
                        if (successResponse.data.code === 200) {
                            this.$message({
                                message: '修改成功',
                                type: 'success'
                            });
                            this.$store.commit('setUserInfo', this.form);
                            this.isButtonClicked = true;
                        }
                    })
                    .catch(failResponse => {
                    })
            },
            cancel() {
                this.isButtonClicked = true;
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
    
        }
    };
</script>