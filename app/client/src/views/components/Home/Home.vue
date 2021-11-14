<template>
  <Main>
    <button @click="getProfile">プロフィール取得</button>
    <el-scrollbar height="auto">
      <p v-for="item in 20" :key="item" class="scrollbar-demo-item">
        <Entry />
      </p>
    </el-scrollbar>
    <div class="home"></div>
  </Main>
</template>

<script lang="ts" src="./Home.ts"></script>

<style scoped lang="scss" src="./Home.scss"></style>
