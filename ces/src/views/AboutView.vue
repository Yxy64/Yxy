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
          v-for="item in list1.data.users"
          :key="item.id"
          :label="item.username"
          :value="item.cok_lsp"
        />
      </el-select>
         <el-input
        v-model="currentPage"
        placeholder="请输入页数(默认1000条一页)"
        style="width: 203px"
      ></el-input>

      <el-button @click="load" type="primary">搜索</el-button>
<el-button size="small" type="primary" @click="exportExcel"
      >导出excel</el-button
    >
<el-tag type="warning">SKU总数{{ list2s.skuCount }}</el-tag>
      <el-table
      id="out-table"
        ref="multipleTableRef"
        :data="list2"
        style="width: 100%; height: 95%; overflow-y: auto"
      >
        <el-table-column label="商家SKU" width="120" property="ware.outSkuId" />
        <el-table-column property="ware.skuName" label="商品名称" width="240" />
        <el-table-column
           label="图片地址"
           min-width="200">
           <template slot-scope="scope">
             <p>http://img10.360buyimg.com/o2o{{scope.row.imageUrl }}</p>
           </template>
    </el-table-column>
        <el-table-column label="图片">
          <template #default="scope">
            <el-popover placement="top-start" title="" trigger="hover">
              <img
                slot="reference"
                :src="`http://img10.360buyimg.com/o2o` + scope.row.imageUrl"
                style="width: 30px; height: 30px"
              />
            </el-popover>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import FileSaver from "file-saver";
import XLSX from "xlsx";
export default {
  data() {
    return {
      value: "",
      list1: [],
      list2: [],
      list2s: [],
      multipleTableRef: [],
      currentPage:"1"
    };
  },
  created() {
    this.selectlb();
  },
  watch: {},
  mounted() {},
  methods: {
    load() {
      document.cookie = this.value;
      this.$axios({
        method: "POST",
        url: '/api/client?appName=scpc&functionId=enterprise/skuList&body={"pageNo":"'+this.currentPage+'","pageSize":"1000"}',
      }).then((res) => {
        this.list2 = res.data.result.list;
         this.list2s = res.data.result;
        console.log(this.list2);
      });
    },
    selectlb() {
      var getData = require("../../static/data.json");
      this.list1 = getData;
    },
    exportExcel() {
      var xlsxParam = { raw: true };
      var wb = XLSX.utils.table_to_book(
        document.querySelector("#out-table"),
        xlsxParam
      );
      var wbout = XLSX.write(wb, {
        bookType: "xlsx",
        bookSST: true,
        type: "array",
      });
      try {
        FileSaver.saveAs(
          new Blob([wbout], { type: "application/octet-stream" }),
          "SKU商品.xlsx"
        );
      } catch (e) {
        if (typeof console !== "undefined") console.log(e, wbout);
      }
      return wbout;
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