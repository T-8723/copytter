<template>
  <el-header>
    <el-row>
      <el-col :span="2">
        <el-avatar :size="50" :src="circleUrl"></el-avatar>
      </el-col>

      <el-col :span="20" class="author-name">{{ user?.username }}</el-col>

      <el-col :span="2">
        <el-popover placement="left" :width="400" trigger="click">
          <template #reference>
            <el-button circle>
              <el-icon>
                <more />
              </el-icon>
            </el-button>
          </template>
        </el-popover>
      </el-col>
    </el-row>
  </el-header>
  <el-main>
    <p class="entry-body">{{ entry.body }}</p>
  </el-main>

  <el-footer>
    <el-row>
      <el-col :span="12">
        <div class="footer-relation-cont">
          <el-icon>
            <refresh-left />
          </el-icon>
          {{ entry.relation_cont }}
        </div>
      </el-col>
      <el-col :span="12">
        <div class="footer-like-cont">
          <el-icon>
            <star />
          </el-icon>
          {{ entry.like_count }}
        </div>
      </el-col>
    </el-row>
  </el-footer>
</template>

<script lang="ts" src="./Entry.ts"></script>

<style scoped lang="scss" src="./Entry.scss"></style>
