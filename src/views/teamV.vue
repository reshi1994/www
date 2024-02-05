<script lang="ts" setup>

</script>

<template>
  <div class="main-container">
    <div class="pd-ltr-20 xs-pd-20-10">
      <div class="min-height-200px">
        <div class="page-header">
          <div class="row">
            <div class="col-md-12 col-sm-12">
              <div class="title">
                <h4>Rehabilitation Teams</h4>
              </div>
              <nav aria-label="breadcrumb" role="navigation">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item"><a href="/home">Home</a></li>
                  <li class="breadcrumb-item active" aria-current="page">Teams</li>
                </ol>
              </nav>
            </div>
          </div>
        </div>
        <!-- Fade-in effect -->
        <h5 class="h4 text-blue mb-10">We Have Experienced Rehabilitation Teams</h5>
        <p class="mb-30"><code>Click. </code>team member to acquire patients info</p>
        <div class="row clearfix">

<!--          从服务器获取信息-->



<!--          卡片结构    用来显示成员信息-->
          <div class="col-lg-3 col-md-6 col-sm-12 mb-30" v-for="(member, index) in [1,2,3,4,5]" :key="index">
            <div class="da-card">
              <div class="da-card-photo">
                <img src="vendors/images/photo1.jpg" alt="">
                <div class="da-overlay">
                  <div class="da-social">
                    <ul class="clearfix">
                      <li><a href="#"><i class="fa fa-wechat"></i></a></li>
                      <li><a href="#"><i class="fa fa-phone"></i></a></li>
                      <li><a href="#"><i class="fa fa-envelope-o"></i></a></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="da-card-content">
                <h5 class="h5 mb-10" :names="member">Don H. Rabon</h5>
                <p class="mb-0">Lorem ipsum dolor sit amet</p>
              </div>
            </div>
          </div>

          <div class="col-lg-3 col-md-6 col-sm-12 mb-30">
            <div class="da-card">
              <div class="da-card-photo">
                <img src="vendors/images/photo2.jpg" alt="">
                <div class="da-overlay">
                  <div class="da-social">
                    <ul class="clearfix">
                      <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                      <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                      <li><a href="#"><i class="fa fa-envelope-o"></i></a></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="da-card-content">
                <h5 class="h5 mb-10">Don H. Rabon</h5>
                <p class="mb-0">Lorem ipsum dolor sit amet</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-12 mb-30">
            <div class="da-card">
              <div class="da-card-photo">
                <img src="vendors/images/photo3.jpg" alt="">
                <div class="da-overlay">
                  <div class="da-social">
                    <ul class="clearfix">
                      <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                      <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                      <li><a href="#"><i class="fa fa-envelope-o"></i></a></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="da-card-content">
                <h5 class="h5 mb-10">Don H. Rabon</h5>
                <p class="mb-0">Lorem ipsum dolor sit amet</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-12 mb-30">
            <div class="da-card">
              <div class="da-card-photo">
                <img src="vendors/images/photo4.jpg" alt="">
                <div class="da-overlay">
                  <div class="da-social">
                    <ul class="clearfix">
                      <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                      <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                      <li><a href="#"><i class="fa fa-envelope-o"></i></a></li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="da-card-content">
                <h5 class="h5 mb-10">Don H. Rabon</h5>
                <p class="mb-0">Lorem ipsum dolor sit amet</p>
              </div>
            </div>
          </div>
        </div>



      </div>
      <div class="footer-wrap pd-20 mb-20 card-box">
        DeskApp - Bootstrap 4 Admin Template. <a target="_blank" href="http://www.mobanwang.com/" title="模板王">模板王</a>
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">

</style>