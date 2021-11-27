<template>
  <el-container>
    <el-header>ユーザー情報登録</el-header>
    <el-main>
      <div class="form-box">
        <el-alert
          title="入力された情報では登録出来ません"
          type="error"
          center
          show-icon
          v-if="!regist_check"
        ></el-alert>
        <el-form ref="refForm" :model="form" status-icon :rules="rules" label-width="180px">
          <el-form-item label="ユーザーID">
            <el-popover
              placement="bottom"
              title="ユーザーID"
              :width="600"
              trigger="hover"
              content="自身のアカウントを表すCopytter上でユニークなIDです。任意の値を入力できます。"
            >
              <template #reference>
                <el-input v-model="form.profile_user_id"></el-input>
              </template>
            </el-popover>
          </el-form-item>
          <el-form-item label="プロフィール">
            <el-popover
              placement="bottom"
              title="プロフィール"
              :width="200"
              trigger="hover"
              content="自身の紹介文です。"
            >
              <template #reference>
                <el-input v-model="form.profile_message" :rows="6" type="textarea"></el-input>
              </template>
            </el-popover>
          </el-form-item>

          <el-form-item>
            <el-button @click="registProfile">登録</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-main>
    <!-- <el-footer>Footer</el-footer> -->
  </el-container>
</template>

<script lang="ts" src="./Profile.ts"></script>

<style scoped lang="scss" src="./Profile.scss"></style>
