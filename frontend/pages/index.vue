<template>
  <body class="font-mono">
    <div :class="blurClass" class="flex justify-start xl:justify-center items-center h-screen bg-white/30 transition-all duration-500">
      <div class="flex justify-center items-start flex-col p-6">
        <h1 class="text-xl">📚unauthenticated</h1>
        <h1 class="text-6xl font-bold mb-8">Nuxt3 + Fastapi <br> Login Template</h1>
        <p class="text-lg mb-4 w-1/2 min-w-96">This is a login example template built with Nuxt3 and FastAPI. You can use this template as a starting point to build your own application.</p>
        <p class="text-lg mb-4">Click the buttons below to log in or sign up for a new account.</p>
        <div class="flex flex-row">
          <NuxtLink to="/SignIn" class="flex items-center justify-center w-20 p-2 m-2 bg-zinc-700 text-white text-center rounded-lg shadow-md">Login ❯</NuxtLink>
          <NuxtLink to="/SignUp" class="flex items-center justify-center w-20 p-2 m-2 text-black text-center border rounded-lg bg-white opacity-65 hover:opacity-100">Sign up</NuxtLink>
        </div>
      </div>
    </div>
  </body>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const blurClass = ref('backdrop-blur-none');

onMounted(() => {
  setTimeout(() => {
    blurClass.value = 'backdrop-blur-sm';
  }, 500); // 100ms 延迟可以调整
});
</script>

<style scoped>
/* 确保过渡效果的平滑 */
.transition-all {
  transition: all 0.5s ease-in-out;
}
</style>
