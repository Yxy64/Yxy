<template>
  <div>
    <label class="lab">关键字</label>
    <Input placeholder="请输入关键字" style="width: 180px" v-model="query.content" />
    <el-button type="primary" icon="el-icon-search" style="margin-left:20px;" @click="showSouSuo">搜索</el-button>
    <el-button plain icon="el-icon-refresh" @click="showEmpty">重置</el-button>

    <el-table ref="multipleTable" :data="showSJ" tooltip-effect="dark" style="width: 100%" border>
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column label="序号">
        <template slot-scope="scope">{{ scope.row.messageId }}</template>
      </el-table-column>
      <el-table-column prop="content" label="消息内容"></el-table-column>
      <el-table-column prop="ctime" label="发送日期"></el-table-column>
      <el-table-column label="操作">
        <template>
          <el-button type="text">收件人列表</el-button>
          <el-button type="text" class="del" @click="Delete">删除</el-button>
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
      total: 0,
      size: 0,
      currentPage4: 1,
      showSJ: [],
      query: {
        content: ""
      },
      messageId: ""
    };
  },
  mounted() {
    this.showShuJu();
  },
  created() {
    this.showFenYe();
  },
  methods: {
    //   显示
    showShuJu() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/sms-message/admin/getSendMessageList?offset=1&limit=10`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.showSJ = result.data.data.records;
      });
    },
    //   查询
    showSouSuo() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/sms-message/admin/getSendMessageList?offset=1&limit=10&content=${this.query.content}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.showSJ = result.data.data.records;
      });
    },
    // 重置{
    showEmpty() {
      this.query = {
        content: ""
      };
      this.showShuJu();
    },
    // 删除
    Delete() {
      var that = this;
      this.$axios({
        url: "http://122.112.253.28:8085/api/sms-message/admin/delMessage",
        method: "post",
        data: {
          messageId: that.messageId
        },
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
    },
    handleSizeChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/sms-message/admin/getSendMessageList?offset=1&limit=${val}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data.records;
      });
    },
    handleCurrentChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/sms-message/admin/getSendMessageList?offset=${val}&limit=10`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data.records;
      });
    },
    showFenYe() {
      this.$axios({
        method: "GET",
        url:
          "http://122.112.253.28:8085/api/users/admin/getBackUsersList?offset=1&limit=10",
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.total = result.data.data.total;
        this.size = result.data.data.size;
        this.showSJ = result.data.data.records;
      });
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
.lab {
  padding: 0 12px;
}
.del {
  color: #f5222d;
}
.block {
  text-align: right;
  height: 50px;
  line-height: 50px;
  padding-top: 11px;
}
</style>