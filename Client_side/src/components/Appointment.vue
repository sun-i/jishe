<template>
    <el-container>
        <el-header class="head">
                <h3>NAME 检测</h3>
                <el-input placeholder="请输入内容" class="input-with-select" size="small" v-model="input1">
                    <el-button slot="append" icon="el-icon-search" size="small"></el-button>
                </el-input>
                <el-link class="el-icon-s-tools" :underline="false"></el-link>
                <el-link class="el-icon-switch-button" :underline="false"></el-link>
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
            <el-menu router default-active="/appointment" class="el-menu-vertical-demo" active-text-color="#66b1ff">
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
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{ path: '/patientIndex' }">患者</el-breadcrumb-item>
                    <el-breadcrumb-item><a href="#">预约诊断</a></el-breadcrumb-item>
                </el-breadcrumb>
                <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                    <el-form-item label="预约人账号">
                        <el-input v-model="ruleForm.username" :disabled=true></el-input>
                    </el-form-item>
                    <el-form-item label="预约人姓名" prop="name">
                        <el-input v-model="ruleForm.name"></el-input>
                    </el-form-item>
                    <el-form-item label="选择医生" prop="doctorId">
                        <el-button :type="chooseDoctorFlag" style="width:100%" @click="doctorDialogTableVisible = true">{{ chooseDoctorText }}</el-button>
                    </el-form-item>

                    <el-dialog title="预约医生信息" :visible.sync="doctorDialogTableVisible" width="70%">
                                <el-table
                                        :data="doctorData"
                                        border
                                        style="width: 100%">
                                    <el-table-column property="name" label="姓名" width="150"></el-table-column>
                                    <el-table-column property="phone" label="联系方式" width="150"></el-table-column>
                                    <el-table-column property="email" label="联系邮箱" width="200"></el-table-column>
                                    <el-table-column property="address" label="联系地址"></el-table-column>
                                    <el-table-column
                                            fixed="right"
                                            label="操作"
                                            width="100">
                                        <template slot-scope="scope">
                                            <el-button @click="handleClick(scope.row.name, scope.row.id)" type="text"
                                                       size="small">预约
                                            </el-button>
                                            <el-button type="text" size="small">联系</el-button>
                                        </template>
                                    </el-table-column>
                                </el-table>

                            </el-dialog>

                    <el-form-item label="预约时间" required>
                        <el-form-item prop="reserve_time">
                            <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.reserve_time" style="width: 100%;"></el-date-picker>
                        </el-form-item>
                    </el-form-item>
                    <el-form-item label="上传图像" prop="imageId">
                        <el-upload
                            class="upload-demo"
                            action=""
                            :http-request="uploadImage"
                            :file-list="fileList">
                            <el-button :type="uploadWavFlag" style="width: 100%;">{{ uploadWavText }}</el-button>
                        </el-upload>
                    </el-form-item>
                    <el-form-item label="备注">
                        <el-input v-model="ruleForm.remark"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                        <el-button @click="resetForm('ruleForm')">重置</el-button>
                    </el-form-item>
                </el-form>
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
    .main .el-form {
        padding: 60px;
        padding-top: 30px;
        margin: 20px;
        background-color: #fff;
        border-radius: 10px;
    }

    .el-form-item >>> .el-upload {
        width: 100%;
    }

</style>
  
<script>
    import { mapState } from 'vuex'
    export default {
        name: 'Appointment',
        data() {
            return {
                input1: '',
                circleUrl: "https://img.imgdd.com/f210f3.55703645-a467-4fea-b91c-40c74bd30aad.png",
                ruleForm: {
                    username:this.$store.state.user.username,
                    name: '',
                    doctorId: '',
                    reserve_time: '',
                    remark: '',
                    imageId: '',
                },
                rules: {
                    name: [
                        { required: true, message: '请输入姓名', trigger: 'blur' }
                    ],
                    doctorId: [
                        { required: true, message: '请选择医生', trigger: 'blur' },
                    ],
                    reserve_time: [
                        { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
                    ],
                    imageId: [
                        { required: true, message: '请上传图像', trigger: 'blur' }
                    ]
                },
                fileList: [],
                doctorDialogTableVisible: false,
                doctorData: [],
                chooseDoctorText: "选择医生",
                chooseDoctorFlag: "primary",
                uploadWavText: '上传图像',
                uploadWavFlag: 'primary',
            }
        },
        computed: {
        ...mapState({
                userInfo: state => state.user,
            })
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    let that = this;
                if (valid) {
                    this.$axios.post('patient/create/',
                    this.$qs.stringify({
                                'patientId': that.$store.state.user.id,
                                'doctorId': that.ruleForm.doctorId,
                                'imageId': that.ruleForm.imageId,
                                'reserve_time': that.ruleForm.date,
                                'remark': that.ruleForm.remark,
                                'name': that.ruleForm.name
                            }), {
                                headers : {
                                    'Content-Type': 'application/x-www-form-urlencoded'
                                }
                            }).then(function (data) {
                            data = data.data;
                            if (data.code === 200) {
                                that.$message.success('预约创建成功');
                                // setTimeout(_ => {
                                //     that.$router.push('/patient_index/record');
                                // }, 300);
                            } else {
                                that.$message.error(data.msg);
                            }
                        }).catch(function (err) {
                            that.$message.error('创建预约失败')
                        });
                } else {
                    console.log('error submit!!');
                    return false;
                }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
                this.uploadWavText = "上传图像";
                this.uploadWavFlag = "primary";
                this.chooseDoctorText = "请选择预约医生";
                this.chooseDoctorFlag = "primary";
            },
            uploadImage(file) {
                let that = this;
                let fileReq = new FormData();
                fileReq.append('image', file.file);
                fileReq.append('username', this.$store.state.user.username);
                this.$axios.post('/image/upload/', fileReq, {
                    headers : {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                })
                .then(function (data) {
                    data = data.data;
                    if (data.code === 400) {
                        that.$notify.error({
                            title: '错误',
                            message: '文件上传错误！'
                        });
                    } else if (data.code === 200) {
                        console.log(data);
                        that.ruleForm.imageId = data.imageId;
                        that.uploadWavText = '已成功上传图像文件';
                        that.uploadWavFlag = 'success';
                        that.$notify({
                            title: '成功',
                            message: '文件上传成功',
                            type: 'success'
                        });
                    }
                }).catch(err => {
                    that.$notify.error({
                        title: '错误',
                        message: '上传文件出现异常！'
                    });
                })
            },
            handleClick(name, id) {
                this.ruleForm.doctorId = id;
                this.doctorDialogTableVisible = false;
                this.chooseDoctorText = "已选择预约医生 (" + name + ")";
                this.chooseDoctorFlag = "success";
            },
        },

        mounted() {
            let that = this;
            this.ruleForm.name = this.$store.state.user.name;
            this.$axios.get('user/doctor/all/').then(function (data) {
                data = data.data;
                console.log(data);
                that.doctorData = data.list;
            }).catch(function (err) {
                that.$message.error('加载医生信息失败');
            })
        }
    };
</script>