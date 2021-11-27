<template>
  <el-container>
    <el-aside width="auto">
      <el-menu default-active="2" :collapse="isCollapse" @open="handleOpen" @close="handleClose">
        <el-sub-menu index="1">
          <template #title>
            <el-icon><location /></el-icon>
            <span>Navigator One</span>
          </template>
          <el-menu-item-group>
            <template #title><span>Group One</span></template>
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="Group Two">
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-4">
            <template #title><span>item four</span></template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="2">
          <el-icon><icon-menu /></el-icon>
          <template #title>Navigator Two</template>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <el-icon><document /></el-icon>
          <template #title>Navigator Three</template>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <template #title>Navigator Four</template>
        </el-menu-item>
      </el-menu></el-aside
    >
    <el-container>
      <el-header class="header-container">
        <el-link v-if="visibleOnlyLoginedUser" @click="toAuth">ログイン</el-link>
        <el-row v-if="!visibleOnlyLoginedUser">
          <el-col :span="1">
            <el-avatar :size="50" :src="circleUrl"></el-avatar>
          </el-col>
          <el-col :span="22" class="author-name">{{ profile?.user?.username }}</el-col>
          <el-col :span="1">
            <el-popover placement="left" :width="400" trigger="click">
              <template #reference>
                <el-button circle class="menu-button">
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
        <el-affix v-if="!visibleOnlyLoginedUser" :offset="88">
          <el-input v-model="textarea" :rows="5" type="textarea" placeholder="Please input" />
          <el-button class="send_button" type="primary" @click="sendEntry">投稿</el-button>
        </el-affix>
        <slot></slot>
      </el-main>
    </el-container>
  </el-container>
</template>

<script src="./Main.ts"></script>

<style lang="scss" src="./Main.scss"></style>
