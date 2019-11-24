<template>
  <div class="app-container">
    <!--卡片视图区域-->
    <el-card>
      <!--搜索及添加区域-->
      <el-row :gutter="20" class="head-container">
        <el-col :span="6">
          <el-input placeholder="请输入内容" size="small">
            <el-button slot="append" icon="el-icon-search" />
          </el-input>
        </el-col>
        <el-col :span="3">
          <el-button type="primary" size="small">添加</el-button>
        </el-col>
      </el-row>

      <!--表格区域-->
      <el-table :data="userInfo" size="small" border style="width: 100%">
        <el-table-column type="index" />
        <el-table-column prop="image" label="头像" width="50px">
          <template slot-scope="scope">
            <img :src="scope.row.image" class="el-avatar">
          </template>
        </el-table-column>
        <el-table-column prop="username" label="用户名" />
        <el-table-column prop="real_name" label="姓名" />
        <el-table-column prop="email" label="邮箱" />
        <el-table-column prop="is_active" label="状态">
          <template slot-scope="scope">
            <el-switch v-model="scope.row.is_active" />
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" size="small" icon="el-icon-edit" />
            <el-button type="danger" size="small" icon="el-icon-delete" />
            <el-button type="warning" size="small" icon="el-icon-setting" />
          </template>
        </el-table-column>
      </el-table>
      <!--分页区域-->
      <el-pagination
        :current-page="queryInfo.page"
        :page-sizes="[5, 10, 20, 30, 40, 50, 100]"
        :page-size="queryInfo.size"
        layout="total, sizes, prev, pager, next, jumper"
        :total="count"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        class="footer-container"
      />
    </el-card>

  </div>
</template>

<script>
import { UserList } from '@/api/user'
export default {
  data() {
    return {
      userInfo: [],
      count: 0,
      queryInfo: {
        page: 1,
        size: 10
      }

    }
  },
  created() {
    this.getUserList()
  },
  methods: {
    getUserList() {
      UserList(this.queryInfo).then(response => {
        console.log(response)
        this.userInfo = response.results
        this.count = response.count
      })
    },
    handleSizeChange(newSize) {
      this.queryInfo.size = newSize
      this.getUserList()
    },
    handleCurrentChange(newPage) {
      this.queryInfo.page = newPage
      this.getUserList()
    }
  }
}
</script>
<style lang="less" scoped>

</style>
