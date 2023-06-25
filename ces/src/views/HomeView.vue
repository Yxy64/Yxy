<template>
  <div class="home">
    <!-- <button @click="load2">修改</button> -->

    <div class="box">
      <el-select
        v-model="value"
        class="m-2"
        placeholder="账号选择"
        size="large"
      >
        <el-option
          v-for="item in list.data.users"
          :key="item.id"
          :label="item.username"
          :value="item.cok_lsp"
        />
      </el-select>
      <el-input
        v-model="currentPage"
        placeholder="请输入页数"
        style="width: 203px"
      ></el-input>

      <el-select
        v-model="time1"
        class="m-2"
        placeholder="起始时间"
        size="large"
      >
        <el-option
          v-for="item in time1s.data.users"
          :key="item.time"
          :label="item.time"
          :value="item.time"
        />
      </el-select>

      <el-select
        v-model="time2"
        class="m-2"
        placeholder="结束时间"
        size="large"
      >
        <el-option
          v-for="item in time2s.data.users"
          :key="item.time"
          :label="item.time"
          :value="item.time"
        />
      </el-select>

      <el-button @click="load" type="primary">搜索</el-button>
      <el-button @click="load2" type="primary">修改</el-button>
      <el-button @click="load3" type="primary">清除</el-button>
      <el-tag type="warning">门店总数{{ list2s.totalCount }}&nbsp;&nbsp;&nbsp;&nbsp;【50为一页，懒得做分页】</el-tag>

      <el-table
        ref="multipleTableRef"
        :data="list2"
        style="width: 100%; height: 95%; overflow-y: auto"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column label="门店ID" width="120" property="id" />
        <el-table-column property="stationName" label="门店名称" width="240" />
        <el-table-column
          property="stationAddress"
          label="门店地址"
          width="650"
        />
        <el-table-column property="cityName" label="所在城市" width="200" />
        <el-table-column property="countyName" label="所在县区" width="200" />
        <el-table-column
          property="serviceTimeStart1"
          label="营业时间"
          show-overflow-tooltip
        />
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      value: "",
      list: [],
      getData: "",
      getData1: "",
      getData2: "",
      list2: [],
      list2s: [],
      checked: [],
      totalCounts: "",
      currentPage: "", // 当前页码
      pageSize: 50, // 每页的数据条数
      multipleSelection: [],
      liid: [],
      time1s: [],
      time2s: [],
      time1: "",
      time2: "",
    };
  },
  created() {
    this.selectlb();
  },
  watch: {

  },
  mounted() {},
  methods: {
    load() {
      document.cookie = this.value;
      this.$axios({
        method: "get",
        url:
          "/api/client?appName=scpc&functionId=storeNew/queryPageList&body={pageSize:" +
          this.pageSize +
          ",pageNo:" +
          this.currentPage +
          ",pageSizes:[1,10,20,30,40,50,100]}",
      }).then((res) => {
        this.list2 = res.data.result.list;
        this.list2s = res.data.result;
        // console.log(this.list2s);
      });
    },
    selectlb() {
      var getData = require("../../static/data.json");
      this.list = getData;

      var getData1 = require("../../static/time.json");
      this.time1s = getData1;

      var getData2 = require("../../static/time2.json");
      this.time2s = getData2;
      // console.log(this.list);
    },
    handleSelectionChange(val) {
      // this.multipleSelection = val;
      val.forEach((item) => {
        const id = item.id;
        if (this.multipleSelection.indexOf(id) == -1) {
          this.multipleSelection.push(id);
        }
      });
      console.log(this.multipleSelection);
    },
    load2() {
      document.cookie = this.value;
      this.$axios({
        method: "get",
        url:
          '/api/client?appName=scpc&functionId=storeNew/batchUpdateStoreInfo&body={"setupType":1,"ids":"' +
          this.multipleSelection +
          '","serviceTimeStart1":"' +
          this.time1 +
          '","serviceTimeEnd1":"' +
          this.time2 +
          '"}',
      }).then((res) => {
        if (res.data.code == "0") {
          this.$message({
            message: "修改成功!",
            type: "success",
          });
          this.multipleSelection = [];
          this.load();
        } else {
          this.$message.error("修改失败!");
          this.multipleSelection = [];
          this.load();
        }
      });
    },
    load3() {
      this.multipleSelection = [];
      this.value = "";
      this.currentPage = "";
      this.time1 = "";
      this.time2 = "";
      console.log(this.multipleSelection);
    },
  },
};
</script>
<style scoped>
.home {
  height: 100%;
}
.box {
  height: 100%;
}
</style>