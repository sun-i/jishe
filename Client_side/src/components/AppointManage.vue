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
            <el-menu router default-active="/appointManage" class="el-menu-vertical-demo"  active-text-color="#66b1ff" :default-openeds="['1']">
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
                    <el-breadcrumb-item><a href="#">预约管理</a></el-breadcrumb-item>
                </el-breadcrumb>
                <el-table
                    :data="tableData.filter(data => !searchData || data.patient_name.toLowerCase().includes(searchData.toLowerCase()))"
                    class="recordTable">
                    <el-table-column
                    label="预约编号"
                    width="100px" type="index">
                    </el-table-column>
                    <el-table-column
                    label="病人姓名"
                    prop="patient_name" width="120px">
                    </el-table-column>
                    <el-table-column
                    label="联系方式"
                    prop="phone" width="120px">
                    </el-table-column>
                    <el-table-column
                    label="邮箱"
                    prop="email" width="170px">
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
                    align="right" width="250px">
                    <template slot="header" slot-scope="scope">
                        <el-input 
                        v-model="searchData"
                        size="small"
                        placeholder="输入病人姓名搜索"/>
                    </template>
                    </el-table-column>
                </el-table>
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

    .main .recordTable {
        margin: 20px;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
    }
    .main >>> .el-table {
        width: 96%;
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
                tableData: [],
                searchData: '',
                patientInfo: {}
            }
        },
        computed: {
        ...mapState({
                userInfo: state => state.user,
            })
        },
        methods: {
            getCurrentTime(date) {
                const isoDate = new Date(date);
                const year = isoDate.getFullYear();
                const month = ('0' + (isoDate.getMonth() + 1)).slice(-2);
                const day = ('0' + isoDate.getDate()).slice(-2);
                const hours = ('0' + isoDate.getHours()).slice(-2);
                const minutes = ('0' + isoDate.getMinutes()).slice(-2);
                const seconds = ('0' + isoDate.getSeconds()).slice(-2);
                return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
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
            this.patientInfo = this.$store.state.user
            let that = this
            let url = '/patient/list/' + that.patientInfo.id
            this.$axios.get(url).then(function (data) {
                data = data.data;
                console.log(data);
                that.tableData = data.list;
                for(let i = 0 ; i < that.tableData.length; i ++ ) {
                    that.tableData[i].reserve_time = that.getCurrentTime(that.tableData[i].reserve_time);
                }
            }).catch(function (err) {
                console.log(err);
                that.$message.error('获取挂号记录失败');
            });
        }
    };
</script>