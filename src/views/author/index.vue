    <template>
  <div class="app-container">
    <!-- 添加作者信息按钮 -->
    <el-row :gutter="10" class="mb8">
<!--      <el-col :span="1.5">-->
<!--        <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>-->
<!--      </el-col>-->
      <toolbar @search="getAuthorListByID" @reset="reSet" @add="handleAdd" ></toolbar>
    </el-row>
    <br/>
    <!--作者信息列表 -->
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column prop="id" label="序号" width="180"></el-table-column>
      <el-table-column prop="first_name" label="姓名"></el-table-column>
      <el-table-column prop="last_name" label="笔名"></el-table-column>
      <el-table-column label="操作" width="180" align="center">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="open(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
      <template #empty>
        <div style="line-height: 26px">暂无数据~</div>
      </template>

    </el-table>
    <!--添加作者信息表单-->
    <el-dialog :title="title" :visible.sync="centerDialogVisible" width="50%" center>
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item
          prop="first_name"
          label="作者姓名"
          :rules="[
            { required: true, message: '请输入作者姓名', trigger: 'change' }
          ]"
        >
          <el-input v-model="form.first_name"></el-input>
        </el-form-item>
        <el-form-item
          prop="last_name"
          label="作者笔名"
          :rules="[{ required: true, message: '请输入作者笔名', trigger: 'change' }
          ]"
        >
          <el-input v-model="form.last_name"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancel">取 消</el-button>
        <el-button type="primary" @click="submitForm('form')">确 定</el-button>
      </span>
    </el-dialog>
    <!--删除 二次确认弹窗-->

  </div>
</template>

<script>
import {
  createAuthorInfo,
  getAuthorInfo,
  // getAuthorInfoById,
  UpdateAuthorInfoById,
  DeleteAuthorInfoById,
  getAuthorListById
} from '@/api/author'

export default {
  data() {
    return {
      tableData: [],
      title: '',

      centerDialogVisible: false,
      form: {
        first_name: '',
        last_name: ''
      }
    }
  },
  mounted() {
    this.getAuthorList()
  },
  methods: {
    handleAdd() {
      this.title = '添加作者信息'
      this.centerDialogVisible = true
    },
    // 弹窗中的取消按钮事件
    cancel() {
      this.centerDialogVisible = false
      this.reset()
    },
    // 重置表单数据
    reset() {
      this.form = {
        first_name: '',
        last_name: ''
      }
    },
    // 弹窗中的确定按钮,调用接口保存作者信息
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          if (this.title === '添加作者信息') {
            this.handleCreate()
          } else {
            this.handleUpdate()
          }
          this.centerDialogVisible = false
          // alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    // 删除二次确认弹窗
    open(index, row) {
      this.$confirm('此操作将删除该内容, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.handleDelete(index, row)
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    // 添加用户
    handleCreate() {
      createAuthorInfo(this.form).then(res => {
        if (res.rspInf === 'success') {
          this.$message.success('添加成功')
          this.getAuthorList()
        } else {
          this.$message.error('添加失败')
        }
      })
        .catch(err => {
          this.$message.error('服务端异常，添加失败。')
        })
    },
    // 根据用户ID进行查询
    getAuthorListByID(searchKey) {
      // debugger
      console.log(searchKey)
      if (searchKey.length >= 1) {
        getAuthorListById(searchKey).then(res => {
          if (res.rspInf === 'success') {
            this.$message.success('查询成功')
            console.log(res.responseData)
            this.tableData = res.responseData
          } else {
            this.$message.error('查询失败')
          }
        })
          .catch(err => {
            this.$message.error('服务端异常，查询失败。')
          })
      } else {
        this.getAuthorList()
      }
    },
    // 用户信息更新
    handleUpdate() {
      console.log(this.form)
      UpdateAuthorInfoById(this.form).then(res => {
        if (res.rspInf === 'success') {
          this.$message.success('更新成功')
          this.getAuthorList()
        } else {
          this.$message.error('更新失败')
        }
      })
        .catch(err => {
          this.$message.error('服务端异常，更新失败。')
        })
    },

    // 删除用户信息
    handleDelete(index, row) {
      const auhtorId = row.id
      DeleteAuthorInfoById(auhtorId).then(res => {
        if (res.rspInf === 'success') {
          this.$message.success('删除成功')
          this.getAuthorList()
        } else {
          this.$message.error('删除失败')
          this.getAuthorList()
        }
      })
        .catch(err => {
          this.$message.error('删除失败，catch')
          this.getAuthorList()
        })
    },
    // 获取用户信息
    getAuthorList() {
      getAuthorInfo()
        .then(res => {
          if (res.rspInf === 'success') {
            console.log(res.responseData)
            this.tableData = res.responseData
          } else {
            this.$message.error('获取信息失败')
          }
        })
        .catch(err => {
          this.$message.error('服务端异常，请联系管理员解决。')
        })
    },
    reSet() {
      this.getAuthorList()
    },
    handleEdit(index, row) {
      this.centerDialogVisible = true
      this.title = '编辑作者信息'
      this.form = { ...row }
    }
  }
}

</script>

<style>
</style>
