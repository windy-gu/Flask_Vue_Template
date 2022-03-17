<template>
  <div>
    <!--工具栏-->
    <div class="head-container">
      <div>
        <!--搜素-->
        <span>
          <el-input v-model="searchKey" clearable placeholder="输入序号搜索" style="width: 200px;" class="filter-item" @keyup.enter.native="toQuery" />
          <span class="filter-item">
            <el-button type="success" icon="el-icon-search" @click="toQuery">搜索</el-button>
            <el-button type="warming" icon="el-icon-refresh" @click="reset">重置</el-button>
            <el-button type="primary" icon="el-icon-plus" @click="add">添加</el-button>
          </span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
  },
  data() {
    return {
      searchKey: ''
    }
  },
  methods: {
    toQuery() {
      // debugger
      this.$emit('search', this.searchKey)
    },
    add() {
      this.$emit('add')
    },
    reset() {
      this.searchKey = ''
      this.$emit('reset')
    }
  }
}
</script>

<style lang="scss" scoped>
// 工具栏
.head {
  &-container {
    text-indent: -10px;
    > div {
      display: flex;
      align-items: center;
      justify-content: space-between;
      > span {
        display: flex;
        align-items: center;
      }
      .filter {
        &-item {
          margin-left: 10px;
        }
      }
    }
  }
}
</style>
