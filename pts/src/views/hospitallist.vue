<template>
  <div>
    <div class="nav-top">
      <label class="lab">医院名称</label>
      <Input placeholder="请输入医院名称" style="width: 180px" v-model="query.hospitalName" />
      <label class="lab">详细地址</label>
      <Input placeholder="请输入详细地址" style="width: 180px" v-model="query.address" />
      <label class="lab">管理员姓名</label>
      <Input placeholder="请输入管理员姓名" style="width: 180px" v-model="query.directorName" />
      <label class="lab">管理员手机号</label>
      <Input placeholder="请输入管理员手机号" style="width: 180px" v-model="query.directorPhone" />
      <label class="lab">代理商姓名</label>
      <Select style="width:200px" class="sele" v-model="query.agentId">
        <Option v-for="(item,key) in DaiLi" :key="key" :value="item.agentId">{{item.companyName}}</Option>
      </Select>
      <el-button
        type="primary"
        icon="el-icon-search"
        style="margin-left:20px;"
        @click="showSouSuo"
      >搜索</el-button>
      <el-button plain icon="el-icon-refresh" @click="showEmpty">重置</el-button>
    </div>

    <el-table ref="multipleTable" :data="showSJ" tooltip-effect="dark" style="width: 100%" border>
      <el-table-column type="index" label="序号"></el-table-column>
      <el-table-column prop="hospitalName" label="医院名称"></el-table-column>
      <el-table-column label="详细地址">
        <template slot-scope="scope">{{scope.row.province}}{{scope.row.city}}{{scope.row.area}}{{scope.row.address}}</template>
      </el-table-column>
      <el-table-column prop="directorName" label="管理员姓名"></el-table-column>
      <el-table-column prop="directorPhone" label="管理员手机号"></el-table-column>
      <el-table-column prop="deposit" label="押金"></el-table-column>
      <el-table-column prop="deviceCount" label="设备数量"></el-table-column>
      <el-table-column prop="sumTurnover" label="总收入"></el-table-column>
      <el-table-column prop="companyName" label="代理商姓名"></el-table-column>
      <el-table-column label="收费规则">
        <template>
          <el-button type="text">用床套餐</el-button>
          <el-button type="text">超时扣费</el-button>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template>
          <el-button type="text">解绑</el-button>
          <el-button type="text">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        background
        @current-change="handleCurrentChange"
        :current-page="currentPage4"
        :page-sizes="[10, 20, 50, 100]"
        :page-size="10"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      ></el-pagination>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      DaiLi: [],
      showSJ: [],
      total: 0,
      size: 0,
      currentPage4: 1,
      query: {
        hospitalName: "",
        address: "",
        directorName: "",
        directorPhone: "",
        agentId: ""
      }
    };
  },
  mounted() {
    this.showDaiLi();
    this.showShuJu();
  },
  methods: {
    showDaiLi() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/agent/admin/getAllAgentList`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.DaiLi = result.data.data;
      });
    },
    // 查询
    showSouSuo() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/hospital/admin/getHospitalList?offset=1&limit=10&hospitalName=${this.query.hospitalName}&address=${this.query.address}&agentId=${this.query.agentId}&directorPhone=${this.query.directorPhone}&directorName=${this.query.directorName}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.showSJ = result.data.data.records;
      });
    },
    // 重置
    showEmpty() {
      this.query = {
        realName: "",
        userPhone: "",
        agentId: ""
      };
    },
    // 显示
    showShuJu() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/hospital/admin/getHospitalList?offset=1&limit=10`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.showSJ = result.data.data.records;
      });
    },
    // 分页
    showFenYe() {
      this.$axios({
        method: "GET",
        url:
          "http://122.112.253.28:8085/api/hospital/admin/getHospitalList?offset=1&limit=10",
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.total = result.data.data.total;
        this.size = result.data.data.size;
        this.showSJ = result.data.data;
      });
    },
    handleSizeChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/hospital/admin/getHospitalList?offset=1&limit=${val}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data;
      });
    },
    handleCurrentChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/hospital/admin/getHospitalList?offset=${val}&limit=10`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data;
      });
    }
  }
};
</script>
<style scoped>
.lab {
  padding: 0 12px;
}
.nav-top {
  margin-bottom: 20px;
}
.block {
  text-align: right;
  height: 50px;
  line-height: 50px;
  padding-top: 11px;
}
</style>