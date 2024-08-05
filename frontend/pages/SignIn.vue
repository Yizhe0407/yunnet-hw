<template>
    <body class="font-mono">
        <div class="flex justify-center items-center h-screen">
            <div class="absolute top-0 left-0 p-8">
                <BackToHome />
            </div>
            <div
                class="flex justify-center items-center flex-col w-96 p-6 backdrop-blur-sm bg-white/30 rounded-2xl shadow-lg">
                <h1 class="text-2xl font-semibold mb-6">Sign in</h1>
                <div v-if="errorMessage"
                    class="flex items-center justify-between p-2 mb-4 w-64 text-sm text-red-700 font-semibold border border-red-400 rounded-lg bg-gradient-to-r from-rose-200 to-rose-50">
                    {{ "⚠️ " + errorMessage }}
                    <button @click="clearErrorMessage"
                        class="p-1 w-6 h-6 flex items-center justify-center rounded bg-transparent hover:bg-rose-200">✕</button>
                </div>
                <input v-model="user.email" placeholder="Email address"
                    class="mb-4 p-2 w-64 border rounded-lg bg-gray-100 focus:outline-none focus:ring-2 focus:border-blue-500" />
                <input type="password" v-model="user.password" placeholder="Password"
                    class="mb-6 p-2 w-64 border rounded-lg bg-gray-100 focus:outline-none focus:ring-2 focus:border-blue-500" />
                <button @click="submit"
                    class="mb-4 w-64 p-2 bg-blue-400 hover:bg-blue-500 text-white rounded-lg shadow-md">Sign in</button>
                <button class="mb-6 text-xs text-stone-300">Forgot your password?</button>
                <h1 class="mb-4 text-base">Don’t have account?</h1>
                <NuxtLink to="/SignUp" class="text-center bg-white p-2 w-64 border rounded-lg shadow hover:shadow-lg">
                    Create new account</NuxtLink>

            </div>
        </div>
    </body>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const handleKeydown = (event) => {
  console.log(event.code);
  if (event.code === 'Enter') {
    submit()
  }
};

onMounted(() => {
  window.addEventListener('keydown', handleKeydown, false);
});

onBeforeUnmount(() => {
  window.removeEventListener('keydown', handleKeydown, false);
});

const user = ref({
    email: '',
    password: ''
})

const errorMessage = ref('')
const router = useRouter()

const submit = async () => {
    if (!user.value.email || !user.value.password) {
        errorMessage.value = 'Email and password cannot be empty'
        return
    }

    try {
        errorMessage.value = '' // 清空之前的错误信息
        const data = await $fetch('http://localhost:8000/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: { email: user.value.email, password: user.value.password }
        })

        if (data.status === 'success') {
            router.push({
                path: '/PersonalHomepage',
                query: { name: data.name, email: data.email }
            })
        } else if (data.status === 'error') {
            errorMessage.value = data.detail
        }
    } catch (error) {
        console.error('Error:', error)
        errorMessage.value = 'Failed to sign in'
    }
}

const clearErrorMessage = () => {
    errorMessage.value = ''
}
</script>