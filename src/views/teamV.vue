<script lang="ts" setup>
import {teamHooks, teamProperty} from '@/store/team'
import {toRefs} from "vue";
const {teamMembers} = toRefs(teamProperty)
const {reqTeamMembers} = teamHooks()
reqTeamMembers()
</script>

<template>
  <!-- Team Start -->
  <div class="container-fluid team py-6">
    <div class="container">
      <div class="text-center wow bounceInUp" data-wow-delay="0.1s">
        <small
            class="d-inline-block fw-bold text-dark text-uppercase bg-light border border-primary rounded-pill px-4 py-1 mb-3">Our
          Team</small>
        <h1 class="display-5 mb-5">We have experienced Rehab Team</h1>
      </div>
      <div class="row g-4">
        <div class="col-lg-3 col-md-6 wow bounceInUp" data-wow-delay="0.1s" v-for="(member, index) of teamMembers" :key="index">
          <div class="team-item rounded">
            <a href="#" ><img class="img-fluid rounded-top " :src="member.imgSrc" alt=""></a>
            <div class="team-content text-center py-3 bg-dark rounded-bottom">
              <h4 class="text-primary">{{ member.user }}</h4>
              <p class="text-white mb-0">{{ member.title }}</p>
            </div>
            <div class="team-icon d-flex flex-column justify-content-center m-4" @click.prevent="">
              <a class="share btn btn-primary btn-md-square rounded-circle mb-2" href=""><i
                  class="fas fa-share-alt"></i></a>
              <a class="share-link btn btn-primary btn-md-square rounded-circle mb-2" href=""><i
                  class="fab fa-facebook-f"></i></a>
              <a class="share-link btn btn-primary btn-md-square rounded-circle mb-2" href=""><i
                  class="fab fa-twitter"></i></a>
              <a class="share-link btn btn-primary btn-md-square rounded-circle mb-2" href=""><i
                  class="fab fa-instagram"></i></a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
  <!-- Team End -->
</template>

<style scoped lang="less">

</style>