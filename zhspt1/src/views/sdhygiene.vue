<template>
  <div>
    <div class="nav-top">
      <label class="lab">卫生检查日期</label>
      <el-date-picker
        v-model="query.checkDate"
        type="date"
        placeholder="选择日期"
        value-format="yyyy-MM-dd"
        format="yyyy-MM-dd"
      ></el-date-picker>
      <el-button
        type="primary"
        icon="el-icon-search"
        style="margin-left:20px;"
        @click="showSouSuo"
      >搜索</el-button>
      <el-button plain icon="el-icon-refresh" @click="showEmpty">重置</el-button>
    </div>
    <el-row class="el_row_1">
      <el-button type="primary" icon="el-icon-plus" @click="add">新增</el-button>
      <el-button type="success" icon="el-icon-edit">修改</el-button>
      <el-button type="danger" icon="el-icon-delete">删除</el-button>
    </el-row>
    <!-- 显示 -->
    <el-table ref="multipleTable" :data="str" tooltip-effect="dark" style="width: 100%">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column label="序号" width="120">
        <template slot-scope="scope">{{ scope.row.id }}</template>
      </el-table-column>
      <el-table-column prop="checkDate" label="卫生检查日期"></el-table-column>
      <el-table-column prop="buildingNo" label="宿舍栋号"></el-table-column>
      <el-table-column prop="storey" label="楼层"></el-table-column>
      <el-table-column prop="dormitoryNo" label="宿舍号"></el-table-column>
      <el-table-column prop="deductIds" label="卫生扣分项"></el-table-column>
      <el-table-column prop="totalPdeduct" label="总扣分"></el-table-column>
      <el-table-column prop="totalScore" label="总得分"></el-table-column>
      <el-table-column prop="modifyTime" label="创建时间"></el-table-column>
      <!-- 操作 -->
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="success" icon="el-icon-edit" circle @click="update(scope.row.id)"></el-button>
          <el-button type="danger" icon="el-icon-delete" circle @click="Delete(scope.row.id)"></el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 增加 -->
    <el-dialog title="添加宿舍信息" :visible.sync="dialogFormVisible">
      <el-form ref="addFrom" :model="addFrom" label-width="80px">
        <label class="lab">卫生检查日期</label>
        <el-date-picker
          v-model="addFrom.checkDate"
          type="date"
          placeholder="选择日期"
          value-format="yyyy-MM-dd"
          format="yyyy-MM-dd"
          :label="xs.checkDate"
        ></el-date-picker>
        <br />
        <br />
        <label class="lab">宿舍栋号</label>
        <Select style="width:200px" class="sele" v-model="addFrom.buildingNo">
          <Option v-for="(item,key) in list2" :key="key" :value="item.dictValue">{{item.dictLabel}}</Option>
        </Select>
        <br />
        <br />
        <label class="lab">宿舍楼层</label>
        <Select style="width:200px" class="sele" v-model="addFrom.storey">
          <Option v-for="(item,key) in list3" :key="key" :value="item.dictValue">{{item.dictLabel}}</Option>
        </Select>
        <br />
        <br />
        <label class="lab" @click="showSuShe">宿舍号</label>
        <Select style="width:200px" class="sele" v-model="addFrom.dormitoryNo">
          <Option v-for="(item,key) in list4" :key="key" :value="item.dormitoryNo">{{item.dormitoryNo}}</Option>
        </Select>
        <br />
        <br />
        <label class="lab">卫生项</label>
        <el-select v-model="addFrom.deductOption" multiple placeholder="请选择">
          <el-option
            v-for="item in list5"
            :key="item.value"
            :label="item.deductOption"
            :value="item.id"
          ></el-option>
        </el-select>
        <br />
        <br />
        <label class="lab">描述信息</label>
        <Input placeholder="请输入描述信息" style="width: 180px" v-model="addFrom.remark" />
        <el-form-item style="float:right">
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button @click="xsqx">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>
import moment from "moment";
export default {
  data() {
    return {
      pageNum: 1,
      pageSize: 10,
      dialogFormVisible: false,
      dialogFormVisible2: false,
      str: [],
      list1: [],
      list2: [],
      list3: [],
      list4: [],
      list5: [],
      query: {
        checkDate: ""
      },
      addFrom: {
        checkDate: "",
        buildingNo: "",
        storey: "",
        dormitoryNo: "",
        deductOption: "",
        remark: ""
      },
      xs: {
        checkDate: "",
        buildingNo: []
      }
    };
  },
  computed: {},
  mounted() {
    this.showShuJu();
    this.showKouFenXiang();
    this.showDongHao();
    this.showLouCen();
    this.showWeiSheng();
  },
  methods: {
    //   数据初始化加载
    showShuJu() {
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/smartdor/sdhygiene/list?pageNum=1&pageSize=10`,
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
    showKouFenXiang() {
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/sysset/hygienededuct/listAll`,
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          that.list1 = response.data.data.list;
        })
        .catch(error => {});
    },
    // 删除
    Delete(id) {
      var that = this;
      this.$axios({
        url:
          "http://122.112.253.28:8095/prod-api/smartdor/sdhygiene/deleteByIds/" +
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
    },
    // 搜索
    showSouSuo() {
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/smartdor/sdhygiene/list?pageNum=1&pageSize=10&checkDate=${that.query.checkDate}`,
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        },
        data: {
          checkDate: that.query.checkDate
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
        checkDate: ""
      };
      this.showShuJu();
    },
    // 搜索栋号
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
          that.list2 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 修改
    update(id) {
      this.dialogFormVisible2 = true;
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/smartdor/sdhygiene/${id}`,
        method: "GET",

        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          this.xs = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    add() {
      this.dialogFormVisible = true;
    },
    // 搜索楼层
    showLouCen() {
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
          that.list3 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 搜索宿舍号
    showSuShe() {
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/basedata/bdormitory/getBDormitoryListByCol?buildingNo=${that.addFrom.buildingNo}&storey=${that.addFrom.storey}`,
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
    },
    // 卫生
    showWeiSheng() {
      var that = this;
      this.$axios({
        url: `http://122.112.253.28:8095/prod-api/sysset/hygienededuct/listAll`,
        method: "GET",
        headers: {
          Authorization: window.sessionStorage.token
        }
      })
        .then(response => {
          console.log(response.data);
          that.list5 = response.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    xsqx() {
      this.dialogFormVisible = false;
      this.addFrom = {
        checkDate: "",
        buildingNo: "",
        storey: "",
        dormitoryNo: "",
        deductOption: "",
        remark: ""
      };
    },
    // 增加
    onSubmit() {
      var that = this;
      this.$axios({
        url: "http://122.112.253.28:8095/prod-api/smartdor/sdhygiene/create",
        method: "POST",
        data: {
          checkDate: that.addFrom.checkDate,
          buildingNo: that.addFrom.buildingNo,
          storey: that.addFrom.storey,
          bdormitoryId: that.addFrom.dormitoryNo,
          deductIds: that.addFrom.deductOption,
          remark: that.addFrom.remark
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
          this.showShuJu();
        } else {
          this.$message({
            type: "info",
            message: "添加失败"
          });
        }
      });

      this.addFrom = {
        checkDate: "",
        buildingNo: "",
        storey: "",
        dormitoryNo: "",
        deductOption: "",
        remark: ""
      };
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