<template>
  <div class="div_d">
    <div class="div_d1">
      <div class="block">
        <span class="demonstration">卫生检查日期</span>
        <el-date-picker
          v-model="qk.checkDate"
          type="date"
          placeholder="选择日期"
          value-format="yyyy-MM-dd"
          format="yyyy-MM-dd"
        ></el-date-picker>

        <el-button type="primary" icon="el-icon-search" @click="Chax" class="el_button_1">查询</el-button>
        <el-button plain icon="el-icon-refresh" @click="qingk">重置</el-button>
      </div>
    </div>

    <div class="div_d3">
      <el-row class="el_row_1">
        <el-button type="danger" icon="el-icon-delete">删除</el-button>
      </el-row>

      <div class="div_d4">
        <el-table ref="multipleTable" :data="jb" tooltip-effect="dark" style="width: 100%">
          <el-table-column type="selection" width="55"></el-table-column>
          <el-table-column label="序号" width="120">
            <template slot-scope="scope">{{ scope.row.id }}</template>
          </el-table-column>
          <el-table-column prop="studentNo" label="设备出入类型"></el-table-column>
          <el-table-column prop="studentNo" label="学号"></el-table-column>
          <el-table-column prop="className" label="班级"></el-table-column>
          <el-table-column prop="studentName" label="学生姓名"></el-table-column>
          <el-table-column prop="dorAddress" label="宿舍信息"></el-table-column>
          <el-table-column prop="modifyTime" label="考勤时间"></el-table-column>
          <el-table-column prop="modifyTime" label="考勤状态"></el-table-column>
          <el-table-column prop="createTime" label="创建时间"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button type="info" icon="el-icon-edit" circle></el-button>
              <el-button type="danger" icon="el-icon-delete" circle @click="Delete(scope.row.id)"></el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      textarea: "",
      list1: [],
      list2: [],
      list3: [],
      list4: [],
      jb: [],
      rules: {
        name: [
          { required: true, message: "班级名称不能为空", trigger: "blur" }
        ],
        region: [
          { required: true, message: "班主任不能为空", trigger: "change" }
        ]
      },
      dialogFormVisible2: false,
      pageNum: 1,
      pageSize: 100,
      qk: {
        modifyTime: ""
      },
    };
  },
  mounted() {
    this.xiala1();
    this.xiala2();
    this.xiala4();
    this.xians();
  },
  methods: {
    xiala1() {
      var that = this;
      that
        .$axios({
          url:
            "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_building",
          method: "GET",
          headers: {
            Authorization: window.sessionStorage.token
          }
        })
        .then(response => {
          that.list1 = response.data.data;
        });
    },

    xiala2() {
      var that = this;
      that
        .$axios({
          url:
            "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/sys_storey",
          method: "GET",
          headers: {
            Authorization: window.sessionStorage.token
          }
        })
        .then(response => {
          that.list2 = response.data.data;
        });
    },

    xiala3() {
      var that = this;
      that
        .$axios({
          url: `http://122.112.253.28:8095/prod-api/basedata/bdormitory/getBDormitoryListByCol?buildingNo=${that.ruleForm.buildingNo}&storey=${that.ruleForm.storey}`,
          method: "GET",
          headers: {
            Authorization: window.sessionStorage.token
          }
        })
        .then(response => {
          that.list3 = response.data.data;
        });
    },

    xiala4() {
      var that = this;
      that
        .$axios({
          url:
            "http://122.112.253.28:8095/prod-api/sysset/hygienededuct/listAll",
          method: "GET",
          headers: {
            Authorization: window.sessionStorage.token
          }
        })
        .then(response => {
          // console.log(response);
          that.list4 = response.data.data;
        });
    },

    xians() {
      var that = this;
      that
        .$axios({
          url:
            "http://122.112.253.28:8095/prod-api/smartdor/sdAttence/list?pageNum=1&pageSize=10",
          method: "GET",
          headers: {
            Authorization: window.sessionStorage.token
          }
        })
        .then(response => {
          // console.log(response)
          that.jb = response.data.data.list;
        });
    },

    Delete(id) {
      var that = this;
      that
        .$axios({
          url:
            "http://122.112.253.28:8095/prod-api/smartdor/sdAttence/deleteByIds/" +id,
          method: "DELETE",
          headers: {
            Authorization: window.sessionStorage.token
          }
        })
        .then(response => {
          console.log(response);
          if (response.data.code == "200") {
            that.$message({
              type: "success",
              message: "删除成功"
            });
            that.xians();
          } else {
            that.$message({
              type: "info",
              message: "删除失败"
            });
          }
        });
    },

    Chax() {
      var that = this;
      that
        .$axios({
          url: `http://122.112.253.28:8095/prod-api/smartdor/sdAttence/list?pageNum=1&pageSize=10&checkDate=${that.qk.checkDate}`,
          method: "GET",
          headers: {
            Authorization: window.sessionStorage.token
          },
          data: {
            checkDate: that.qk.checkDate
          }
        })
        .then(response => {
          console.log(response)
          that.jb = response.data.data.list;
          // that.xians();
        });
    },

    qingk() {
      this.qk = {
        modifyTime: ""
      };
      this.xians();
    },
  }
};
</script>

<style scoped>
.div_d {
  width: 1641px;
  height: 848px;
}
.div_d1 {
  width: 100%;
  height: 60px;
}
.div_d2 {
  width: 270px;
  height: 58px;
  float: left;
}
.label_1 {
  width: 70px;
}
.div_d3 {
  width: 100%;
  height: 516px;
}
.div_d4 {
  margin-top: 20px;
  width: 100%;
  height: 500px;
}
.div_d6 {
  width: 400px;
  float: left;
}
.div_d7 {
  width: 400px;
  float: left;
}
.div_d8 {
  width: 160px;
  position: absolute;
  left: 681px;
  top: 414px;
}
.sb1 {
  margin-top: 10px;
}
.el_button_1 {
  margin-left: 10px;
}
.lm {
  margin-top: 10px;
}
</style>