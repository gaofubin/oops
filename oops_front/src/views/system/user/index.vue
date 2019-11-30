<template>
  <div class="app-container">
    <!--卡片视图区域-->
    <el-card>
      <!--搜索及添加区域-->
      <el-row :gutter="20" class="head-container">
        <el-col :span="6">
          <el-input v-model="queryInfo.search" placeholder="请输入内容" size="small" clearable @clear="getUserList" @change="getUserList" @input="getUserList">
            <el-button slot="append" icon="el-icon-search" @click="getUserList" />
          </el-input>
        </el-col>
        <el-col :span="3">
          <el-button type="primary" size="small" @click="addUserDialogVisible = true">添加</el-button>
        </el-col>
      </el-row>

      <!--表格区域-->
      <el-table :data="userInfo" size="small" border style="width: 100%">
        <el-table-column type="index" />
        <el-table-column prop="username" label="用户名" />
        <el-table-column prop="real_name" label="姓名" />
        <el-table-column prop="email" label="邮箱" />
        <el-table-column prop="is_active" label="状态">
          <template slot-scope="scope">
            <el-switch v-model="scope.row.is_active" @change="userStateChanged(scope.row)" />
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
        class="footer-container"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </el-card>
    <!--添加用户对话框-->
    <el-dialog title="添加用户" :visible.sync="addUserDialogVisible" width="50%">
      <!--内容主体区域-->
      <el-form ref="addUserFormRef" :model="addUserForm" :rules="addUserFormRule" label-width="70px" class="demo-ruleForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="addUserForm.username" />
        </el-form-item>
        <el-form-item label="姓名" prop="real_name">
          <el-input v-model="addUserForm.real_name" />
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="addUserForm.email" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="addUserForm.password" />
        </el-form-item>
        <el-form-item label="状态" prop="is_active">
          <el-radio v-model="addUserForm.is_active" label="true">激活</el-radio>
          <el-radio v-model="addUserForm.is_active" label="false">锁定</el-radio>
        </el-form-item>
      </el-form>
      <!--内容底部区域-->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addUserDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUserSubmit">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
import { UserList, modifyUserState, UserAdd } from '@/api/user'
export default {
  data() {
    return {
      userInfo: [],
      count: 0,
      queryInfo: {
        search: '',
        page: 1,
        size: 10
      },
      // 控制添加对话框显示与隐藏
      addUserDialogVisible: false,
      // 添加用户表单数据
      addUserForm: {
        username: '',
        password: '',
        email: '',
        real_name: '',
        is_active: false
      },
      // 添加表单的验证规则
      addUserFormRule: {}
    }
  },
  created() {
    this.getUserList()
  },
  methods: {
    getUserList() {
      UserList(this.queryInfo).then(response => {
        this.userInfo = response.detail.results
        this.count = response.detail.count
      })
    },
    handleSizeChange(newSize) {
      this.queryInfo.size = newSize
      this.getUserList()
    },
    handleCurrentChange(newPage) {
      this.queryInfo.page = newPage
      this.getUserList()
    },
    // 监听switch状态的改变
    userStateChanged(userinfo) {
      modifyUserState(userinfo.id, userinfo).then(res => {
        if (res.code !== 200) {
          userinfo.is_active = !userinfo.is_active
          return this.$message.error('更新用户状态失败')
        } else {
          return this.$message.success('更新用户状态成功')
        }
      })
    },
    addUserSubmit() {
      UserAdd(this.addUserForm).then(res => {
        if (res.code === 201) {
          this.addUserDialogVisible = false
          this.getUserList()
          return this.$message.success('添加用户成功')
        } else {
          return this.$message.error('添加用户失败')
        }
      })
    }
  }
}
</script>
<style lang="less" scoped>

</style>
