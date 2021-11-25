<template>
  <Main>
    <el-scrollbar v-if="entries.length > 0" height="100">
      <div v-for="entry in entries" :key="entry.id">
        <Entry :entry="entry" />
      </div>
    </el-scrollbar>
    <el-empty v-else :image-size="150" description="description"></el-empty>
  </Main>
</template>

<script lang="ts" src="./Home.ts"></script>

<style scoped lang="scss" src="./Home.scss"></style>
