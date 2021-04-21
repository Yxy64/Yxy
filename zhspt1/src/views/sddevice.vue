<template>
  <div>
    <div class="nav-top">
      <label class="lab">学员名称</label>
      <Input placeholder="请输入学员名称" style="width: 180px" v-model="query.deviceName" />
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
      <el-table-column prop="deviceIpAddress" label="设备IP地址"></el-table-column>
      <el-table-column prop="deviceAccessType" label="设备出入类型"></el-table-column>
      <el-table-column prop="deviceNo" label="设备号"></el-table-column>
      <el-table-column prop="deviceName" label="设备名称"></el-table-column>
      <el-table-column prop="attenceRuleName" label="考勤规则"></el-table-column>
      <el-table-column prop="status" label="状态">
        <template slot-scope="scope">
          <div>
            <div style="position:relative;z-index:999">
              <el-switch v-model="scope.row.status" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
            </div>
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="createTime" label="创建时间"></el-table-column>
      <!-- 操作 -->
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="success" icon="el-icon-edit" circle @click="update(scope.row.id)"></el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      dialogFormVisible: false,
      str: [],
      query: {
        deviceName: ""
      }
    };
  },
  mounted() {
    this.showShuJu();
  },
  methods: {
    //   搜索
    showSouSuo() {},
    // 重置
    showEmpty() {
      this.query = {
        deviceName: ""
      };
    },
    // 数据初始化
    showShuJu() {
      var that = this;
      this.$axios({
        // id:that.jb.id,
        url: `http://122.112.253.28:8095/prod-api/smartdor/sddevice/list?pageNum=1&pageSize=10`,
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          that.str = response.data.data.list;
        })
        .catch(error => {});
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
</style>