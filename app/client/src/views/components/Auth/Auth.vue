<template>
  <el-container>
    <el-header>Copytter - ログイン</el-header>
    <el-main>
      <div class="form-box">
        <el-alert
          title="入力された情報ではログイン出来ません"
          type="error"
          center
          show-icon
          v-if="!auth_check"
        ></el-alert>
        <el-form
          ref="refForm"
          :model="form"
          status-icon
          :rules="rules"
          label-width="180px"
          @keydown.enter="login"
        >
          <el-form-item label="ユーザー">
            <el-input v-model="form.username"></el-input>
          </el-form-item>

          <el-form-item label="パスワード" prop="pass">
            <el-input
              v-model="form.pass"
              type="password"
              autocomplete="off"
              placeholder="Please input password"
              show-password
            ></el-input>
          </el-form-item>

          <el-form-item label="パスワード(確認)" prop="checkPass">
            <el-input
              v-model="form.checkPass"
              type="password"
              autocomplete="off"
              placeholder="Please input password"
              show-password
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="login">ログイン</el-button>
            <el-button @click="cancel">キャンセル</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-main>
    <!-- <el-footer>Footer</el-footer> -->
  </el-container>
</template>

<script lang="ts" src="./Auth.ts"></script>

<style scoped lang="scss" src="./Auth.scss"></style>
