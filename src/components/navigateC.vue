<script lang="ts" setup>
import {navigateHooks, navigateProperty} from '@/store/navigate'
import {toRefs} from "vue";
const {surName, givenName} = toRefs(navigateProperty.loginedUser)
const {switchDrawer} = navigateHooks()
</script>

<template>
  <!-- Navbar start -->
  <div class="container-fluid nav-bar">
    <div class="container">
      <nav class="navbar navbar-light navbar-expand-lg py-4">
        <a href="#" class="navbar-brand" @click.prevent="switchDrawer">
          <h1 class="text-primary fw-bold mb-0">{{ surName }}<span class="text-dark">{{ givenName }}</span> </h1>
        </a>
        <button class="navbar-toggler py-2 px-3" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarCollapse">
          <span class="fa fa-bars text-primary"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <div class="navbar-nav mx-auto">
            <a href="/" class="nav-item nav-link active">Home</a>
            <a href="/team" class="nav-item nav-link">Teams</a>
            <a href="" class="nav-item nav-link">Services</a>
            <a href="" class="nav-item nav-link">Events</a>
            <a href="" class="nav-item nav-link">Menu</a>
            <div class="nav-item dropdown">
              <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Pages</a>
              <div class="dropdown-menu bg-light">
                <a href="" class="dropdown-item">Booking</a>
                <a href="" class="dropdown-item">Our Blog</a>
                <a href="" class="dropdown-item">Our Team</a>
                <a href="" class="dropdown-item">Testimonial</a>
                <a href="" class="dropdown-item">404 Page</a>
              </div>
            </div>
            <a href="" class="nav-item nav-link">Contact</a>
          </div>
          <button class="btn-search btn btn-primary btn-md-square me-4 rounded-circle d-none d-lg-inline-flex"
                  data-bs-toggle="modal" data-bs-target="#searchModal"><i class="fas fa-search"></i></button>

        </div>
      </nav>
    </div>
  </div>
  <!-- Navbar End -->
</template>

<style scoped lang="less">

</style>