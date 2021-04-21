<template>
    <div class="page-out">
                <Form label-position="right"  :label-width="70">
                    <Row>
                        <Col span="4">
                            <FormItem label="班级名称">
                                <i-input v-model="queryForm.className"></i-input>
                            </FormItem>
                        </Col>
                        <Col span="4" offset="1">
                            <FormItem label="班主任">
                                <i-input v-model="queryForm.classTeacherName"></i-input>
                            </FormItem>
                        </Col>
                        <Col span="4" offset="1">
                            <FormItem label="状态">

                                <Select v-model="queryForm.status" placeholder="班级状态">
                                    <Option v-for="(item,key) in disableList" :key="key" :value="item.dictValue">{{ item.dictLabel }}</Option>
                                </Select>
                            </FormItem>

                        </Col>
                        <Col span="5" >
                            <i-button style="margin-left: 15px" icon="ios-search" type="primary" @click="queryClass">
                                搜索
                            </i-button>
                            <i-button style="margin-left: 15px" icon="md-refresh" @click="reInput">
                                重置
                            </i-button>
                        </Col>
                    </Row>
                </Form>
                <Row>
                    <Col span="24" >
                        <Button type="primary" icon="md-add" @click="add_box = true">
                            新增
                        </Button>
                        <Button type="success" style="margin-left: 10px" icon="ios-create-outline" @click="getClass()">
                            修改
                        </Button>
                        <Button type="error" style="margin-left: 10px" icon="ios-trash">
                            删除
                        </Button>
                    </Col>
                </Row>

        <div class="body">
            <Table border :columns="columns1" :data="data1"></Table>

            <div style="position: relative">
                <Page :total="total" :page-size="pageSize" @on-page-size-change="changePageSize" show-elevator show-sizer style="position: absolute;right: 35px;top:45px" :page-size-opts="opt" @on-change="changePage"/>
            </div>
        </div>


        <Modal
                v-model="add_box"
                title="添加班级信息"
                @on-ok="ok_add"
                @on-cancel="cancel_add"
                width="650px"
        >
            <Form :label-width="60" label-position="right">
               <Row>
                   <Col span="10" offset="0">
                       <FormItem label="班级">
                           <i-input v-model="addForm.className"></i-input>
                       </FormItem>
                   </Col>
                   <Col span="10" offset="1">
                       <FormItem label="班主任">
                           <Select v-model="addForm.classTeacherId">
                               <Option v-for="(item,key) in classTeacherList" :key="key" :value="item.id">{{ item.username }}</Option>
                           </Select>
                       </FormItem>
                   </Col>
               </Row>

            </Form>
        </Modal>

        <Modal
                v-model="update_box"
                title="添加班级信息"
                @on-ok="ok_update"
                @on-cancel="cancel_update"
                width="650px"
        >
            <Form :label-width="60" label-position="right">
                <Row>
                    <Col span="10" offset="0">
                        <FormItem label="班级">
                            <i-input v-model="updateForm.className" disabled></i-input>
                        </FormItem>
                    </Col>
                    <Col span="10" offset="1">
                        <FormItem label="班主任">
                            <Select v-model="updateForm.classTeacherId">
                                <Option v-for="(item,key) in classTeacherList" :key="key" :value="item.id">{{ item.username }}</Option>
                            </Select>
                        </FormItem>
                    </Col>
                </Row>

            </Form>
        </Modal>
    </div>
</template>

<script>
    export default {
        name: 'Bclass',
        data(){
            return {
                updateForm:{
                    className:'',
                    classTeacherId:[]
                },
                addForm:{
                    className:'',
                    classTeacherId:[]
                },
                update_box:false,
                add_box:false,
                opt:[2,5,10],
                queryForm:{
                    className:'',
                    classTeacherName:[],
                    status:[],
                },
                classTeacherList:[],
                pageNum:1,
                pageSize:2,
                total:0,
                totalPage:0,
                columns1: [
                    {
                        type: 'selection',
                        width: 60,
                        align: 'center'
                    },
                    {
                        title: '序号',
                        key: 'id'
                    },
                    {
                        title: '班级名称',
                        key: 'className'
                    },
                    {
                        title: '班主任',
                        key: 'classTeacherName'
                    },
                    {
                        title: '创建时间',
                        key: 'createTime'
                    },
                    {
                        title: '修改时间',
                        key: 'modifyTime'
                    },
                    {
                        title: '状态',
                        key: 'status',
                        render:(h,params) => {
                            return h('i-switch',{
                                props:{
                                    'value':params.row.status === '1',
                                },
                                on:{
                                    'on-change':(status)=>{
                                        this.setDisable(params.row.id,status)
                                    }
                                }
                            })
                        }
                    },
                    {
                        title:'操作',
                        key:'use',
                        render:(h,params) => {
                            return h('div',[
                                h('i-button',{
                                    props:{
                                        type:'success',
                                        icon:'ios-create-outline',
                                        shape:"circle",
                                        size:'small'
                                    },
                                    on:{
                                        click:()=>{
                                            this.getClass(params.row.id);
                                        }
                                    }
                                },''),
                                h('i-button',{
                                    props:{
                                        type:'error',
                                        icon:'ios-trash',
                                        shape:"circle",
                                        size:'small'
                                    },
                                    style:{
                                        'margin-left':'15px'
                                    },
                                    on:{
                                        click:() => {
                                            this.delClasses(params.row.id)

                                        }
                                    }
                                },'')
                            ])
                        }
                    }
                ],
                data1: [],
                disableList:[]
            }
        },
        mounted(){
            this.getClassList();
            this.getDisableList();
            this.getClassTeacherList();
        },
        methods:{
            queryClass(){
                //http://122.112.253.28:8095/prod-api/basedata/bclass/list?pageNum=1&pageSize=10&classTeacherName=%E5%91%A8%E7%8F%8A%E7%8F%8A
                var that = this;
                this.$axios({
                    url:`http://122.112.253.28:8095/prod-api/sys/user/list?pageNum=${that.pageNum}&pageSize=${that.pageSize}&className=${that.queryForm.className}&status=${that.queryForm.status}`,
                    method:'GET',
                    headers:{
                        Authorization:window.sessionStorage.token,
                    },
                    data:{
                        className:that.queryForm.className,
                        status:that.queryForm.status
                    }
                }).then((response) => {
                    that.data1 = response.data.data.list;
                }).catch((error) => {
                    console.log(error)
                })
            },
            ok_update(){
                var that = this;
                // ttp://122.112.253.28:8095/prod-api/basedata/bclass/update/25
                this.$axios({
                    url:`http://122.112.253.28:8095/prod-api/basedata/bclass/update/${this.updateForm.id}`,
                    method:'PUT',
                    data:this.updateForm,
                    headers:{
                        Authorization:window.sessionStorage.token,
                    }
                }).then((response) => {
                    that.success(response.data.message);
                    this.updateForm = {
                        className:'',
                        classTeacherId:[]
                    }
                    that.getClassList();
                }).catch((error) => {
                    console.log(error)
                })
            },
            cancel_update(){
                this.updateForm = {
                    className:'',
                    classTeacherId:[]
                }
            },
            ok_add(){
                //http://122.112.253.28:8095/prod-api/basedata/bclass/create

                var that = this;
                this.$axios({
                    url:'http://122.112.253.28:8095/prod-api/basedata/bclass/create',
                    method:'POST',
                    data:{
                        classTeacherId:that.addForm.classTeacherId,
                        status:'1'
                    },
                    headers:{
                        Authorization:window.sessionStorage.token,
                    }
                }).then((response) => {
                    that.success(response.data.message);
                })

                this.addForm = {
                    className:'',
                    classTeacherName:''
                }
            },
            cancel_add(){
                this.addForm = {
                    className:'',
                    classTeacherName:''
                }
            },
            changePageSize(pageSize){
                this.pageSize = pageSize;
                this.pageNum = 1;
                this.getClassList();
            },
            changePage(pageNum){
                this.pageNum = pageNum;
                this.getClassList();
            },
            getClass(id){
                this.currentUpdateId = id;
                var that = this;
                this.update_box = true;
                //http://122.112.253.28:8095/prod-api/basedata/bclass/25
                this.$axios({
                    url:`http://122.112.253.28:8095/prod-api/basedata/bclass/${id}`,
                    method:'GET',
                    headers:{
                        Authorization:window.sessionStorage.token,
                    }
                }).then((response) => {
                    that.updateForm = response.data.data;
                }).catch((error) => {
                    console.log(error)
                })
            },
            getClassTeacherList(){
              //http://122.112.253.28:8095/prod-api/sys/user/getClassTeacherList
              var that = this;
              this.$axios({
                  url:'http://122.112.253.28:8095/prod-api/sys/user/getClassTeacherList',
                  method:'GET',
                  headers:{
                      Authorization:window.sessionStorage.token,
                  }
              }).then((response) => {
                  that.classTeacherList = response.data.data;
              }).catch((error) => {
                  console.log(error)
              })
            },
            getClassList(){
                const that = this;
                // http://122.112.253.28:8095/prod-api/basedata/bclass/list?pageNum=1&pageSize=10

                this.$axios({
                    url:`http://122.112.253.28:8095/prod-api/basedata/bclass/list?pageNum=${that.pageNum}&pageSize=${that.pageSize}`,
                    method:'GET',
                    headers:{
                        Authorization:window.sessionStorage.token,
                    }
                }).then((response) => {
                    that.data1 = response.data.data.list;
                    that.total = response.data.data.total;
                    that.totalPage = response.data.data.totalPage;
                }).catch((error) => {
                    console.log(error)
                })
            },
            getDisableList(){
                const that = this;
                //http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_normal_disable
                  this.$axios({
                      url:'http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_normal_disable',
                      method:'GET',
                      headers:{
                          Authorization:window.sessionStorage.token,
                      }
                  }).then((response) => {
                      that.disableList = response.data.data;
                  }).catch((error) => {
                      console.log(error)
                  })
            },
            reInput(){
                this.queryForm.className = this.queryForm.classTeacherName = this.queryForm.status = ''
            },
            setDisable(id,status){
                var that = this;
                if(status){
                    status = 1;
                }else{
                    status = 0;
                }
                var result = false;
                // http://122.112.253.28:8095/prod-api/basedata/bclass/update/status/17?status=0
                this.$axios({
                    url:`http://122.112.253.28:8095/prod-api/basedata/bclass/update/status/${id}?status=${status}`,
                    method:'PUT',
                    headers:{
                        Authorization:window.sessionStorage.token,
                    }
                }).then((response) => {
                    if(response.data.code === 200){
                        result = true
                    }else{
                        result = false;
                    }
                    that.success(response.data.message);
                }).catch((error) => {
                    console.log(error)
                })
                return result;
            },
            delClasses(id){
                var that = this;
                //http://122.112.253.28:8095/prod-api/basedata/bclass/deleteByIds/17
                this.$axios({
                    url:`http://122.112.253.28:8095/prod-api/basedata/bclass/deleteByIds/${id}`,
                    method:'DELETE',
                    headers:{
                        Authorization:window.sessionStorage.token,
                    }
                }).then((response) => {
                    if(response.data.code === 200){
                        that.success(response.data.message)
                    }else{
                        that.error(response.data.message)
                    }
                    this.getClassList();
                })
            },
            success (msg) {
                this.$Message.success(msg);
            },
            warning (msg) {
                this.$Message.warning(msg);
            },
            error (msg) {
                this.$Message.error(msg);
            }
        }
    }
</script>

<style>
    .ivu-btn-circle{
        height: 30px!important;
        width: 30px!important;
        text-align: center!important;
        padding-left: 7px!important;
        border-radius: 50%!important;
    }
    .body{
        padding: 25px 0;
    }
    .is-box{
        background-color: #00000033;
        position: fixed;
        height: 100vh;
        width: 100vw;
        top: 0;
        left: 0;
        z-index: 999;
    }
    .is-inner{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
    }
    .ivu-modal-footer{
        border-top: initial!important;
    }
    .ivu-modal-header{
        border-bottom:initial!important;
    }
    .ivu-modal-content{
        border-radius: 3px;
    }
</style>