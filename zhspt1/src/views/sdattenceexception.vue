<template>
  <div>
    <div class="nav-top">
      <label class="lab">学号</label>
      <Input placeholder="请输入学号" style="width: 180px" v-model="query.studentNo" />
      <label class="lab">班级</label>
      <Input placeholder="请输入班级名称" style="width: 180px" v-model="query.className" />
      <label class="lab">学生姓名</label>
      <Input placeholder="请输入学生姓名" style="width: 180px" v-model="query.studentName" />
      <label class="lab">处理状态</label>
      <Select style="width:200px" class="sele" v-model="query.absenceProcessStatus">
        <Option v-for="(item,key) in list" :key="key" :value="item.dictValue">{{item.dictLabel}}</Option>
      </Select>
      <label class="lab">状态</label>
      <Select style="width:200px" class="sele" v-model="query.status">
        <Option v-for="(item,key) in list2" :key="key" :value="item.dictValue">{{item.dictLabel}}</Option>
      </Select>
      <el-button
        type="primary"
        icon="el-icon-search"
        style="margin-left:20px;"
        @click="showSouSuo"
      >搜索</el-button>
      <el-button plain icon="el-icon-refresh" @click="showChongZhi">重置</el-button>
    </div>
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
      <el-table-column prop="studentNo" label="学号"></el-table-column>
      <el-table-column prop="className" label="班级"></el-table-column>
      <el-table-column prop="studentName" label="学生姓名"></el-table-column>
      <el-table-column prop="dorAddress" label="宿舍"></el-table-column>
      <el-table-column prop="absenceProcessStatus" label="处理状态"></el-table-column>
      <el-table-column prop="processPerson" label="处理人"></el-table-column>
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

      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="success" icon="el-icon-edit" circle @click="update(scope.row.id)"></el-button>
          <el-button type="danger" icon="el-icon-delete" circle @click="Delete(scope.row.id)"></el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      str: [],
      list: [],
      list2: [],
      query: {
        studentNo: "",
        className: "",
        studentName: "",
        status: "",
        absenceProcessStatus: ""
      }
    };
  },
  mounted() {
    this.showChuLi();
    this.showZhuangTai();
    this.showShuJu();
  },
  methods: {
    //   数据初始化
    showShuJu() {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/smartdor/exception/list?pageNum=1&pageSize=10",
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          console.log(response.data);
          that.str = response.data.data.list;
        })
        .catch(error => {
          console.log(error);
        });
    },
    //   处理状态
    showChuLi() {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/sys/dict/detail/dictType/absence_process_status",
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
    // 状态
    showZhuangTai() {
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
          console.log(response.data);
          that.list2 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 重置
    showChongZhi() {
      this.query = {
        studentNo: "",
        className: "",
        studentName: "",
        status: "",
        absenceProcessStatus: ""
      };
    },
    // 搜索
    showSouSuo() {},
    // 删除
    Delete(id) {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/smartdor/exception/deleteByIds/" +
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
          this.showShuJu();
        } else {
          this.$message({
            type: "info",
            message: "删除失败"
          });
        }
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
  padding: 0 12px;
}
.el_row_1 {
  margin: 0 20px;
}
</style>