<template>
  <div class="div_d">
    <div class="div_d1">
      <div class="demo-input-suffix div_d2">
        班级名称：
        <el-input placeholder="请输入班级名称" v-model="input1" clearable class="el_input_1"></el-input>
      </div>
      <div class="demo-input-suffix div_d2">
        班主任：
        <el-input placeholder="请输入班主任名称" v-model="input2" clearable class="el_input_1"></el-input>
      </div>
      <div class="demo-input-suffix div_d2">
        状态：
        <el-select v-model="value" placeholder="班级状态">
          <el-option
            v-for="(item,key) in list"
            :key="key"
            :value="item.dictLabel"
          >{{item.dictLabel}}</el-option>
        </el-select>
      </div>
      <el-button type="primary" icon="el-icon-search" @click="sss">搜索</el-button>
      <el-button plain icon="el-icon-refresh" @click="cz">重置</el-button>
    </div>

    <el-row class="el_row_1">
      <el-button type="primary" icon="el-icon-plus" @click="dialogFormVisible = true">新增</el-button>
      <el-button type="success" icon="el-icon-edit">修改</el-button>
      <el-button type="danger" icon="el-icon-delete">删除</el-button>
    </el-row>

    <div class="div_d3">
      <el-table
        ref="multipleTable"
        :data="jb"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column label="序号" width="120">
          <template slot-scope="scope">{{ scope.row.id }}</template>
        </el-table-column>
        <el-table-column prop="className" label="班级名称"></el-table-column>
        <el-table-column prop="classTeacherName" label="班主任"></el-table-column>
        <el-table-column prop="createTime" label="创建时间"></el-table-column>
        <el-table-column prop="modifyTime" label="修改时间"></el-table-column>
        <el-table-column prop="status" label="状态">
          <template slot-scope="scope">
            <div>
              <div style="position:relative;z-index:999">
                <el-switch
                  v-model="scope.row.status"
                  active-color="#13ce66"
                  inactive-color="#ff4949"
                ></el-switch>
              </div>
            </div>
          </template>
        </el-table-column>

        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="success" icon="el-icon-edit" circle @click="update(scope.row.id)"></el-button>
            <el-button type="danger" icon="el-icon-delete" circle @click="Delete(scope.row.id)"></el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <!-- 增加 -->
    <el-dialog title="添加班级信息" :visible.sync="dialogFormVisible">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="班级名称">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="班主任">
          <el-select v-model="form.region" placeholder="请选择" style="width:350px;">
            <el-option
              v-for="(item, key) in list2"
              :key="key"
              :value="item.id"
              :label="item.username"
            >{{ item.username }}</el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button @click="xsqx">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <!-- 修改 -->
    <el-dialog title="修改班级信息" :visible.sync="dialogFormVisible2">
      <el-form ref="from2" :model="from2" label-width="80px">
        <el-form-item label="班级名称">
          <el-input v-model="from2.className" disabled></el-input>
        </el-form-item>
        <el-form-item label="班主任">
          <el-select v-model="from2.classTeacherId" placeholder="请选择" style="width:350px;">
            <el-option
              v-for="(item, key) in list2"
              :key="key"
              :value="item.id"  
              :label="item.username"
            >{{ item.username }}</el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit2">确定</el-button>
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
      input1: "",
      pageNum: 1,
      pageSize: 10,
      input2: "",
      dialogTableVisible: false,
      dialogFormVisible: false,
      dialogFormVisible2: false,
      list: [],
      list2: [],
      value: "",
      value1: "",
      jb: [],
      multipleSelection: [],
      form: {
        name: "",
        region: []
      },
      from2: {
        className: "",
        classTeacherId: []
      }
    };
  },
  mounted() {
    this.xiala();
    this.xians();
    this.xiala2();
  },
  methods: {
    sss() {
      var that = this;
      this.$axios({
        url: ` http://122.112.253.28:8095/prod-api/basedata/bclass/list?pageNum=${that.pageNum}&pageSize=${that.pageSize}&className=${that.input1}&classTeacherName=${that.input2}`,
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        },
        data: {
          className: that.input1,
          classTeacherName: that.input2
        }
      })
        .then(response => {
          that.jb = response.data.data.list;
        })
        .catch(error => {
          console.log(error);
        });
    },
    cz() {
      this.xians();
    },
    xsqx() {
      this.dialogFormVisible = false;
      this.dialogFormVisible2 = false;
    },
    onSubmit() {
      var that = this;
      this.$axios({
        url: "http://122.112.253.28:8095/prod-api/basedata/bclass/create",
        method: "POST",
        data: {
          className: that.form.name,
          classTeacherId: that.form.region,
          status: "1"
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
          this.xians();
        } else {
          this.$message({
            type: "info",
            message: "添加失败"
          });
        }
      });

      this.form = {
        name: "",
        region: ""
      };
    },
    update(id) {
      // console.log(id)
      this.dialogFormVisible2 = true;
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/basedata/bclass/${id}`,
        method: "GET",

        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          this.from2 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    onSubmit2() {
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/basedata/bclass/update/${this.from2.id}`,
        method: "PUT",
        data: that.from2,
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          // that.success(response.data.message);
          if (response.data.code == "200") {
            this.$message({
              type: "success",
              message: "修改成功"
            });
            this.from2 = {
              name2: "",
              region2: []
            };
            this.dialogFormVisible2 = false;
            this.xians();
          } else {
            this.$message({
              type: "info",
              message: "修改失败"
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    xiala() {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_normal_disable",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          that.list = response.data.data;
        })
        .catch(error => {});
    },
    xiala2() {
      var that = this;
      this.$axios({
        url: "http://122.112.253.28:8095/prod-api/sys/user/getClassTeacherList",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          that.list2 = response.data.data;
        })
        .catch(error => {});
    },
    xians() {
      var that = this;
      this.$axios({
        // id:that.jb.id,
        url:
          "http://122.112.253.28:8095/prod-api/basedata/bclass/list?pageNum=1&pageSize=100",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          that.jb = response.data.data.list;
        })
        .catch(error => {});
    },

    Delete(id) {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/basedata/bclass/deleteByIds/" +
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
          this.xians();
        } else {
          this.$message({
            type: "info",
            message: "删除失败"
          });
        }
      });
      // this.$confirm("是否确认删除该的数据项?", "提示", {
      //   confirmButtonText: "确定",
      //   cancelButtonText: "取消",
      //   type: "warning"
      // });
    },

    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },

    handleSelectionChange(val) {
      this.multipleSelection = val;
    }
  }
};
</script>

 <style scoped>
.xzs {
  /* display: none; */
  position: absolute;
  left: 50%;
  top: 0px;
  padding: 32px;
  background: white;
  transform: translate(-50%, 100%);
}
.el_input_1 {
  width: 180px;
}
.div_d1 {
  margin: 10px 32px;
  height: 65px;
}
.div_d2 {
  width: 280px;
  height: 58px;
  float: left;
}
.el_row_1 {
  margin: 0 32px;
  height: 65px;
}
.div_d3 {
  width: 1641px;
}
.sx {
  float: left;
  width: 50px;
}
</style>