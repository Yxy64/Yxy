<template>
  <div class="layout">
    <Layout>
      <Sider ref="side1" hide-trigger collapsible :collapsed-width="78" v-model="isCollapsed">
        <Menu
          active-name="1-2"
          theme="dark"
          width="auto"
          :class="menuitemClasses"
          v-if="list.length > 0"
        >
          <MenuItem name="1" to="/index">
            <img src="../assets/1.png" alt class="tp1" />
            <span class="sp1">智慧宿管云平台</span>
          </MenuItem>
          <Submenu :name="''+key+''" v-for="(item,key) in list" :key="key" :index="''+key+''">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>
              <span>{{ item.meta.title }}</span>
            </template>
            <MenuItem
              :name="(key+2)+'-'+(key2+1)"
              v-for="(item2,key2) in item.children"
              :key="key2"
              :to="''+item2.path+''"
            >{{ item2.meta.title }}</MenuItem>
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

          <span @click="screen" class="sc">
            <i class="iconfont" v-if="!showdon">&#xe662;</i>
            <i class="iconfont" v-if="showdon">&#xe619;</i>
          </span>
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
      visible: false,
      isCollapsed: false,
      list: [],
      showdon: false,
      fullscreen: false // 默认不全屏
    };
  },
  created() {},
  mounted() {
    this.loadData();
  },
  computed: {
    rotateIcon() {
      return ["menu-icon", this.isCollapsed ? "rotate-icon" : ""];
    },
    menuitemClasses() {
      return ["menu-item", this.isCollapsed ? "collapsed-menu" : ""];
    }
  },
  methods: {
    loadData() {
      var that = this;
      this.$axios({
        url: "http://122.112.253.28:8095/prod-api/sys/menu/getRouters",
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
    handleOpen() {
      this.visible = true;
    },
    handleClose() {
      this.visible = false;
    },
    collapsedSider() {
      this.$refs.side1.toggleCollapse();
    },
    screen() {
      this.showdon = !this.showdon;
      let element = document.documentElement;
      if (this.fullscreen) {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        } else if (document.webkitCancelFullScreen) {
          document.webkitCancelFullScreen();
        } else if (document.mozCancelFullScreen) {
          document.mozCancelFullScreen();
        } else if (document.msExitFullscreen) {
          document.msExitFullscreen();
        }
      } else {
        if (element.requestFullscreen) {
          element.requestFullscreen();
        } else if (element.webkitRequestFullScreen) {
          element.webkitRequestFullScreen();
        } else if (element.mozRequestFullScreen) {
          element.mozRequestFullScreen();
        } else if (element.msRequestFullscreen) {
          // IE11
          element.msRequestFullscreen();
        }
      }
      this.fullscreen = !this.fullscreen;
    }
  }
};
</script>

<style scoped>
@font-face {
  font-family: "iconfont"; /* project id 2457007 */
  src: url("//at.alicdn.com/t/font_2457007_eoqy97555vf.eot");
  src: url("//at.alicdn.com/t/font_2457007_eoqy97555vf.eot?#iefix")
      format("embedded-opentype"),
    url("//at.alicdn.com/t/font_2457007_eoqy97555vf.woff2") format("woff2"),
    url("//at.alicdn.com/t/font_2457007_eoqy97555vf.woff") format("woff"),
    url("//at.alicdn.com/t/font_2457007_eoqy97555vf.ttf") format("truetype"),
    url("//at.alicdn.com/t/font_2457007_eoqy97555vf.svg#iconfont") format("svg");
}
.sc {
  cursor: pointer;
  width: 24px;
  height: 24px;
  font-size: 18px;
}
.nr{
  margin: 32px;
}
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
.jt {
  position: fixed;
  right: -120px;
  top: 0px;
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
.tp1 {
  width: 32px;
  height: 32px;
  margin-top: -5px;
}
.nr {
  background: white;
  height: 100vh;
}
.sp1 {
  position: relative;
  top: -10px;
  left: 10px;
}
</style>