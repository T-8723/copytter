import { Module } from "vuex";

import { SelfProfile } from "@/common/services/openapi";

export const UserhModule: Module<{ user: SelfProfile }, unknown> = {
  namespaced: true,
  state: {
    user: {
      id: 0,
      gender: undefined,
      birth_date: undefined,
      location: undefined,
      age: undefined,
      icon_pass: undefined,
      profile_message: undefined,
      status: undefined,
      profile_user_id: undefined,
      sensitive_entry: undefined,
      profile_first_registed: false,
      user: 0,
    },
  },
  getters: {
    getUser: (state): SelfProfile => {
      return state.user;
    },
  },
  actions: {
    setUser({ commit }, user: SelfProfile) {
      commit("setUser", user);
    },
  },
  mutations: {
    setUser(state, user: SelfProfile) {
      state.user = user;
    },
  },
};
