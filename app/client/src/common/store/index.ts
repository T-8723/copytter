// index.ts
/**
 * 状態管理ストアのメイン設定ファイル
 * - 各コンポーネント間で値をやり取りするために状態管理ストアを利用する
 *
 * @module common-store-main
 */

import { createStore } from "vuex";
import { AuthModule } from "./modules/auth-store";
import { UserhModule } from "./modules/user-store";

/** 状態管理 Store のルート定義オブジェクト */
const store = createStore({
  strict: true,
  modules: {
    auth: AuthModule,
    user: UserhModule,
  },
});

export default store;
