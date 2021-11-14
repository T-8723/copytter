import { Module } from "vuex";

import { AuthInfo } from "@/common/types/common";

function getPayload(accessToken: string): AuthState["user_info"] {
  const base64Url = accessToken.split(".")[1];
  const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
  return JSON.parse(decodeURIComponent(escape(window.atob(base64))));
}

export interface AuthState {
  jwt_token: string;
  user_info: AuthInfo;
}

export const AuthModule: Module<AuthState, unknown> = {
  namespaced: true,
  state: {
    jwt_token: "",
    user_info: {
      username: null,
      email: null,
      exp: null,
      orig_iat: null,
      user_id: null,
    },
  },
  getters: {
    getUserInfo: (state): AuthState["user_info"] => {
      return state.user_info;
    },
    getToken: (state): AuthState["jwt_token"] => {
      return state.jwt_token;
    },
  },
  actions: {
    setUserInfo({ commit }, token: string) {
      const info: AuthState["user_info"] = getPayload(token);
      console.log(info);
      commit("setToken", token);
      commit("setUserInfo", info);
    },
  },
  mutations: {
    setUserInfo(state, info: AuthState["user_info"]) {
      state.user_info = info;
    },
    setToken(state, token: string) {
      state.jwt_token = token;
    },
  },
};
