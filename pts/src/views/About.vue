<template>
  <div class="layout">
    <Layout>
      <Sider ref="side1" hide-trigger collapsible :collapsed-width="78" v-model="isCollapsed">
        <Menu active-name="1-2" theme="light" width="auto" :open-names="['1']">
          <MenuItem name="1-3">
            <Icon type="settings"></Icon>
            <span>首页</span>
          </MenuItem>
          <Submenu name="2">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>用户管理
            </template>
            <MenuItem name="2-1" to="list">用户列表</MenuItem>
            <MenuItem name="2-2" to="message">短信列表</MenuItem>
            <MenuItem name="2-3" to="maintain">维护人员列表</MenuItem>
            <MenuItem name="2-4" to="logistics">陪护床人员列表</MenuItem>
          </Submenu>
          <Submenu name="3">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>医院管理
            </template>
            <MenuItem name="3-1" to="hospitallist">医院列表</MenuItem>
            <MenuItem name="3-2">科室列表</MenuItem>
          </Submenu>
          <Submenu name="4">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>设备管理
            </template>
            <MenuItem name="4-1">设备列表</MenuItem>
            <MenuItem name="4-2">商品列表</MenuItem>
            <MenuItem name="4-3">陪护床格子开关列表</MenuItem>
            <MenuItem name="4-4">补货记录列表</MenuItem>
          </Submenu>
          <Submenu name="5">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>订单管理
            </template>
            <MenuItem name="5-1">陪护床订单列表</MenuItem>
            <MenuItem name="5-2">商品订单列表</MenuItem>
            <MenuItem name="5-3">押金订单列表</MenuItem>
          </Submenu>
          <Submenu name="6">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>财务管理
            </template>
            <MenuItem name="6-1">陪护床订单列表</MenuItem>
            <MenuItem name="6-2">商品订单列表</MenuItem>
            <MenuItem name="6-3">押金订单列表</MenuItem>
          </Submenu>
        </Menu>
      </Sider>
      <Layout>
        <Header :style="{padding: 0}" class="layout-header-bar">
          <Icon
            @click.native="collapsedSider"
            :class="rotateIcon"
            :style="{margin: '0 20px'}"
            type="md-menu"
            size="24"
          ></Icon>
          <!-- .. -->

          <!-- .. -->
        </Header>
        <div class="nr">
          <router-view></router-view>
        </div>
      </Layout>
    </Layout>
  </div>
</template>
<script>
export default {
  data() {
    return {
      list: [],
      meta: [],
      isCollapsed: false,
      value: true
    };
  },
  computed: {
    rotateIcon() {
      return ["menu-icon", this.isCollapsed ? "rotate-icon" : ""];
    },
    menuitemClasses() {
      return ["menu-item", this.isCollapsed ? "collapsed-menu" : ""];
    }
  },
  mounted() {},
  methods: {
    collapsedSider() {
      this.$refs.side1.toggleCollapse();
    }
  }
};
</script>
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}
.layout-header-bar {
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}
.layout-logo-left {
  width: 90%;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  margin: 15px auto;
}
.menu-icon {
  transition: all 0.3s;
}
.rotate-icon {
  transform: rotate(-90deg);
}
.menu-item span {
  display: inline-block;
  overflow: hidden;
  width: 69px;
  text-overflow: ellipsis;
  white-space: nowrap;
  vertical-align: bottom;
  transition: width 0.2s ease 0.2s;
}
.menu-item i {
  transform: translateX(0px);
  transition: font-size 0.2s ease, transform 0.2s ease;
  vertical-align: middle;
  font-size: 16px;
}
.collapsed-menu span {
  width: 0px;
  transition: width 0.2s ease;
}
.collapsed-menu i {
  transform: translateX(5px);
  transition: font-size 0.2s ease 0.2s, transform 0.2s ease 0.2s;
  vertical-align: middle;
  font-size: 22px;
}
.nr {
  height: 872px;
  overflow-x: hidden;
  padding: 32px 32px 0px 32px;
  background: white;
}
.bread {
  position: absolute;
  right: 500px;
  z-index: 999;
}
</style>