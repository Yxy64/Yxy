<template>
  <div>
    <div class="nav-top">
      <label class="lab">学员名称</label>
      <Input placeholder="请输入学员名称" style="width: 180px" v-model="query.studentName" />
      <label class="lab">学号</label>
      <Input placeholder="请输入学号" style="width: 180px" v-model="query.studentNo" />
      <label class="lab">班级</label>
      <Input placeholder="请输入班级" style="width: 180px" v-model="query.className" />
      <label class="lab">宿舍栋号</label>
      <Select style="width:200px" class="sele" v-model="query.buildingNo">
        <Option v-for="(item,key) in list" :key="key" :value="item.dictSort">{{item.dictLabel}}</Option>
      </Select>
      <label class="lab">楼层</label>
      <Select style="width:200px" class="sele" v-model="query.storey">
        <Option v-for="(item,key) in list2" :key="key" :value="item.dictSort">{{item.dictLabel}}</Option>
      </Select>
      <label class="lab">请输入宿舍号</label>
      <Input placeholder="请输入宿舍号" style="width: 180px" v-model="query.dormitoryNo" />
      <br />
      <br />
      <label class="lab">状态</label>
      <Select style="width:200px" class="sele" v-model="query.status">
        <Option v-for="(item,key) in list3" :key="key" :value="item.dictLabel">{{item.dictLabel}}</Option>
      </Select>
      <el-button
        type="primary"
        icon="el-icon-search"
        style="margin-left:20px;"
        @click="showSouSuo"
      >搜索</el-button>
      <el-button plain icon="el-icon-refresh" @click="showEmpty">重置</el-button>
    </div>
    <!-- 功能 -->
    <el-row class="el_row_1">
      <el-button type="primary" icon="el-icon-plus" @click="dialogFormVisible = true">新增</el-button>
      <el-button type="success" icon="el-icon-edit">修改</el-button>
      <el-button type="danger" icon="el-icon-delete">删除</el-button>
    </el-row>

    <!-- 显示 -->
    <el-table ref="multipleTable" :data="str" tooltip-effect="dark" style="width: 100%">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column label="序号" width="120">
        <template slot-scope="scope">{{ scope.row.id }}</template>
      </el-table-column>
      <el-table-column prop="studentName" label="学员姓名"></el-table-column>
      <el-table-column prop="studentNo" label="学号"></el-table-column>
      <el-table-column prop="className" label="班级"></el-table-column>
      <el-table-column prop="phone" label="手机号"></el-table-column>
      <el-table-column label="性别">
        <template slot-scope="scope">{{ scope.row.sex === 1 ? '女' : '男' }}</template>
      </el-table-column>
      <el-table-column prop="parentName" label="家长名字"></el-table-column>
      <el-table-column prop="parentPhone" label="家长电话"></el-table-column>
      <el-table-column prop="buildingNo" label="宿舍栋号"></el-table-column>
      <el-table-column prop="storey" label="楼层"></el-table-column>
      <el-table-column prop="dormitoryNo" label="宿舍号"></el-table-column>
      <el-table-column prop="createTime" label="创建时间"></el-table-column>
      <el-table-column prop="status" label="状态">
        <template slot-scope="scope">
          <div>
            <div style="position:relative;z-index:999">
              <el-switch v-model="scope.row.status" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
            </div>
          </div>
        </template>
      </el-table-column>
      <!-- 操作 -->
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="success" icon="el-icon-edit" circle @click="update(scope.row.id)"></el-button>
          <el-button type="danger" icon="el-icon-delete" circle @click="Delete(scope.row.id)"></el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 增加 -->
    <el-dialog title="修改宿舍信息" :visible.sync="dialogFormVisible">
      <el-form ref="addFrom" :model="addFrom" label-width="80px">
        <label class="labs">学员姓名</label>
        <Input
          placeholder="请输入学员姓名"
          style="width: 350px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.studentName"
        />
        <label class="labs">学号</label>
        <Input
          placeholder="请输入学号"
          style="width: 350px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.studentNo"
        />
        <br />
        <label class="labs">班级</label>
        <Input
          placeholder="请输入班级"
          style="width: 350px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.classId"
        />
        <label class="labs">手机号码</label>
        <Input
          placeholder="请输入手机号码"
          style="width: 350px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.phone"
        />
        <br />
        <label class="labs">身份证号</label>
        <Input
          placeholder="请输入身份证号"
          style="width: 340px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.idcard"
        />
        <el-form-item label="性别">
          <el-select v-model="addFrom.sex" placeholder="请选择" style="width:350px;">
            <el-option
              v-for="(item, key) in list4"
              :key="key"
              :value="item.dictSort"
              :label="item.dictLabel"
            >{{ item.dictLabel }}</el-option>
          </el-select>
        </el-form-item>
        <label class="labs">年龄</label>
        <Input
          placeholder="请输入年龄"
          style="width: 350px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.age"
        />
        <label class="labs">家长姓名</label>
        <Input
          placeholder="请输入家长姓名"
          style="width: 350px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.parentName"
        />
        <label class="labs">家长电话</label>
        <Input
          placeholder="请输入家长电话"
          style="width: 350px;margin-left:6px;margin-bottom: 15px;height: 40px;"
          v-model="addFrom.parentPhone"
        />
        <el-form-item label="宿舍栋号">
          <el-select v-model="addFrom.buildingNo" placeholder="宿舍栋号" style="width:350px;">
            <el-option
              v-for="(item, key) in list"
              :key="key"
              :value="item.dictSort"
              :label="item.dictLabel"
            >{{ item.dictLabel }}</el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button @click="xsqx">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      pageNum: 1,
      pageSize: 10,
      dialogFormVisible: false,
      str: [],
      list: [],
      list2: [],
      list3: [],
      list4: [],
      query: {
        studentName: "",
        studentNo: "",
        className: "",
        buildingNo: "",
        storey: "",
        dormitoryNo: "",
        status: ""
      },
      addFrom: {
        studentName: "",
        studentNo: "",
        classId: "",
        phone: "",
        idcard: "",
        sex: "",
        age: "",
        parentName: "",
        parentPhone: "",
        buildingNo: "",
        storey: "",
        dormitoryNo: ""
      }
    };
  },
  mounted() {
    this.showShuJu();
    this.showDongHao();
    this.showLouCeng();
    this.showZhuangTai();
    this.showSex();
  },
  methods: {
    //   宿舍栋号
    showDongHao() {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_building",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          console.log(response.data);
          that.list = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 楼层
    showLouCeng() {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_storey",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          console.log(response.data);
          that.list2 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 状态
    showZhuangTai() {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_student_status",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          console.log(response.data);
          that.list3 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 数据初始化
    showShuJu() {
      var that = this;
      this.$axios({
        // id:that.jb.id,
        url: `http://122.112.253.28:8095/prod-api/basedata/bstudent/list?pageNum=1&pageSize=10`,
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          that.str = response.data.data.list;
        })
        .catch(error => {});
    },
    // 删除
    Delete(id) {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/basedata/bstudent/deleteByIds/" +
          id,
        method: "DELETE",
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(response => {
        // console.log(response)
        if (response.data.code == "200") {
          this.$message({
            type: "success",
            message: "删除成功!"
          });
          this.show();
        } else {
          this.$message({
            type: "info",
            message: "删除失败"
          });
        }
      });
    },
    // 搜索
    showSouSuo() {
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/basedata/bstudent/list?pageNum=1&pageSize=10&studentName=${that.query.studentName}&studentNo=${that.query.studentNo}&className=${that.query.className}&dormitoryNo=${that.query.dormitoryNo}`,
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        },
        data: {
          studentName: that.query.studentName,
          studentNo: that.query.studentNo,
          className: that.query.className,
          dormitoryNo: that.query.dormitoryNo
        }
      })
        .then(response => {
          that.str = response.data.data.list;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 重置
    showEmpty() {
      this.query = {
        studentName: "",
        studentNo: "",
        className: "",
        buildingNo: "",
        storey: "",
        dormitoryNo: "",
        status: ""
      };
      this.showShuJu();
    },
    // 取消
    xsqx() {
      this.dialogFormVisible = false;
    },
    // 新增
    onSubmit() {
      var that = this;
      this.$axios({
        url: "http://122.112.253.28:8095/prod-api/basedata/bstudent/createStu",
        method: "POST",
        data: {
          buildingNo: that.from.buildingNo,
          storey: that.from.storey,
          dormitoryNo: that.from.dormitoryNo,
          dormitoryTeacherId: that.from.dormitoryTeacherId
        },
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(response => {
        if (response.data.code == "200") {
          this.$message({
            type: "success",
            message: "添加成功"
          });
          this.dialogFormVisible = false;
          this.show();
        } else {
          this.$message({
            type: "info",
            message: "添加失败"
          });
        }
      });

      this.from = {
        buildingNo: "",
        storey: "",
        dormitoryTeacherId: "",
        dormitoryNo: ""
      };
    },
    // 性别
    showSex() {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_user_sex",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          console.log(response.data);
          that.list4 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
<style scoped>
.nav-top {
  margin: 20px;
}
.lab {
  text-align: right;
  display: inline-block;
  padding: 0px 12px;
}
.labs {
  text-align: right;
  display: inline-block;
  padding: 0px 12px;
  position: relative;
  top: -10px;
}
.el_row_1 {
  margin: 0 20px;
}
</style>