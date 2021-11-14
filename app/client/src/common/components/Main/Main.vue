<template>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-container>
      <el-header>
        <el-link v-if="visibleLoginButton" @click="toAuth">ログイン</el-link>
      </el-header>
      <el-main><slot></slot></el-main>
    </el-container>
  </el-container>
</template>

<script src="./Main.ts"></script>

<style lang="scss" src="./Main.scss"></style>
