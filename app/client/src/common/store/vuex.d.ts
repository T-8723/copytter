// vuex.d.ts
/**
 * 型定義: ストアアクセス用ののコンポーネントアクセス型拡張設定ファイル
 *
 * @module type-store
 */

import { Store } from "vuex";

declare module "@vue/runtime-core" {
  // provide typings for `this.$store`
  interface ComponentCustomProperties {
    /** Storeへのアクセス用変数定義を追加 */
    $store: Store<unknown>;
  }
}
