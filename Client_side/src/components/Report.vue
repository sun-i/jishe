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
                <el-card class="result">
                    <h4 style="text-align: left;">肿瘤分割结果</h4>
                    <el-row style="margin-top:20px">
                        <el-col span="12">
                            <img :src="image1" alt="" style="width:50%; height:50%">
                            <h5 style="margin-top: 10px;">分割前</h5>
                        </el-col>
                        <el-col span="12">
                            <img :src="image2" alt="" style="width:50%; height:50%">
                            <h5 style="margin-top: 10px;">分割后</h5>
                        </el-col>
                    </el-row>
                    <el-divider></el-divider>
                    <h4 style="text-align: left; margin-top: 30px;">综合诊断结果</h4>
                    <el-row style="margin-top:20px">
                        <div id="chart-container1" style="width: 300px; height: 200px; float: left; margin-left: 100px;"></div>
                        <div id="chart-container2" style="width: 300px; height: 200px; float: left;"></div>
                    </el-row>
                    <el-row>
                        <h4>患者存在肿瘤的概率为{{ probability }}</h4>
                    </el-row>
                    <el-button @click="goto()" type="text"
                                                       size="medium" style="margin-top: 20px;">生成检测报告并撰写病历单
                            </el-button>
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


    .el-col {
        border: 1px solid transparent;
    }

    .result {
        margin: 20px;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
    }
    

</style>
  
<script>
    import * as echarts from 'echarts';
    import { mapState } from 'vuex'
    export default {
        name: 'patientRecord',
        data() {
            return {
                input1: '',
                circleUrl: "https://img.imgdd.com/f210f3.55703645-a467-4fea-b91c-40c74bd30aad.png",
                patientInfo:'',
                active:1,
                image1: 'data:image/jpeg;base64,' + window.localStorage.getItem('img_data1'),
                image2: 'data:image/jpeg;base64,' + window.localStorage.getItem('img_data2'),
                chartInstance: null,
                probability: (window.localStorage.getItem('prob') * 100).toFixed(2) + '%',
            }
        },
        computed: {
        ...mapState({
                userInfo: state => state.user,
            }),
        },
        methods: {
            initChart() {
                const container1 = document.querySelector('#chart-container1')
                const width = container1.clientWidth
                const height = container1.clientHeight

                // 初始化 ECharts 实例并设置容器尺寸
                this.chartInstance = echarts.init(container1)
                this.chartInstance.resize({
                width: width,
                height: height
                })

                this.chartInstance.setOption({
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} <br/>{b}: {c} ({d}%)'
                    },
                    title: {
                        text: '正常' + (100 - window.localStorage.getItem('prob') * 100).toFixed(2) + '%',
                        left: 'center',
                        top: 'center'
                    },
                    legend: {
                        show: false
                    },
                    series: [
                        {
                        name: '诊断结果',
                        type: 'pie',
                        radius: ['45%', '55%'],
                        avoidLabelOverlap: false,
                        label: {
                            show: false
                        },
                        data: [
                            {
                            value: window.localStorage.getItem('prob') * 100,
                            name: '异常',
                            itemStyle: {
                                color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [
                                    {
                                    offset: 0,
                                    color: '#fff'
                                    }
                                ],
                                global: false // 缺省为 false
                                }
                            }
                            },
                            {
                            value: 100 - window.localStorage.getItem('prob') * 100,
                            name: '正常',
                            itemStyle: {
                                color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [
                                    {
                                    offset: 0,
                                    color: '#5EFCE8' // 0% 处的颜色，蓝色
                                    },
                                    {
                                    offset: 1,
                                    color: '#736EFE' // 100% 处的颜色，淡蓝色
                                    }
                                ],
                                global: false // 缺省为 false
                                }
                            }
                            },
                        ]
                        }
                    ]
                    });

                const container2 = document.querySelector('#chart-container2')

                // 初始化 ECharts 实例并设置容器尺寸
                this.chartInstance = echarts.init(container2)
                this.chartInstance.resize({
                width: width,
                height: height
                })

                this.chartInstance.setOption({
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} <br/>{b}: {c} ({d}%)'
                    },
                    title: {
                        text: '异常' + (window.localStorage.getItem('prob') * 100).toFixed(2) + '%',
                        left: 'center',
                        top: 'center'
                    },
                    legend: {
                        show: false
                    },
                    series: [
                        {
                        name: '诊断结果',
                        type: 'pie',
                        radius: ['45%', '55%'],
                        avoidLabelOverlap: false,
                        label: {
                            show: false
                        },
                        data: [
                            {
                            value: 100-window.localStorage.getItem('prob') * 100,
                            name: '正常',
                            itemStyle: {
                                color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [
                                    {
                                    offset: 0,
                                    color: '#fff'
                                    }
                                ],
                                global: false // 缺省为 false
                                }
                            }
                            },
                            {
                            value: window.localStorage.getItem('prob') * 100,
                            name: '异常',
                            itemStyle: {
                                color: {
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [
                                    {
                                    offset: 0,
                                    color: '#5EFCE8' // 0% 处的颜色，蓝色
                                    },
                                    {
                                    offset: 1,
                                    color: '#736EFE' // 100% 处的颜色，淡蓝色
                                    }
                                ],
                                global: false // 缺省为 false
                                }
                            }
                            },
                        ]
                        }
                    ]
                });

            },

            goto(){
                this.$axios.post('detection/reportword/',
                 this.$qs.stringify({
                img_path: window.localStorage.getItem('img_path'),
                recordId: window.localStorage.getItem('record_id'),
                d1: (100-window.localStorage.getItem('prob') * 100).toFixed(2),
                d2: (window.localStorage.getItem('prob') * 100).toFixed(2),
                    })).then(function (data) {
                        data = data.data;
                        if(data.code === 200)
                        {
                            that.$message.success('生成报告成功');
                        }
                        else
                        {
                            that.$message.error('生成报告失败');
                        }
                }).catch(function (err) {
                    console.log(err);
                    that.$message.error('获取挂号记录失败');
                });
                const id = window.localStorage.getItem('record_id');
                this.$router.push('/medicRecord/' + id)
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
            this.initChart()
        }
    };
</script>