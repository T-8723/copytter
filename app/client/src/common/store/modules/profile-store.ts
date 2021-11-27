import { Module } from "vuex";

import { SelfProfile } from "@/common/services/openapi";

export const ProfileModule: Module<{ profile: SelfProfile }, unknown> = {
  namespaced: true,
  state: {
    profile: {
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
      user: {
        id: NaN,
        username: "",
      },
    },
  },
  getters: {
    getProfiler: (state): SelfProfile => {
      return state.profile;
    },
  },
  actions: {
    setProfile({ commit }, profile: SelfProfile) {
      commit("setProfile", profile);
    },
  },
  mutations: {
    setProfile(state, profile: SelfProfile) {
      state.profile = profile;
    },
  },
};
