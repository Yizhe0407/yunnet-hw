<template>

    <body class="font-mono">
        <div class="flex justify-center items-center flex-col h-screen">
            <div class="absolute top-0 left-0 p-8">
                <BackToLogin />
            </div>
            <div
                class="flex justify-center items-center flex-col w-96 p-6 backdrop-blur-sm bg-white/30 rounded-2xl shadow-lg">
                <h1 class="text-2xl font-semibold mb-6">Create an account</h1>
                <div v-if="infoMessage"
                    class="flex items-center justify-between p-2 mb-4 w-64 text-sm text-sky-700 font-semibold border border-sky-400 rounded-lg bg-gradient-to-r from-sky-200 to-sky-50">
                    {{ "⚠️ " + infoMessage }}
                    <button @click="clearinfoMessage"
                        class="p-1 w-6 h-6 flex items-center justify-center rounded bg-transparent hover:bg-sky-200">✕</button>
                </div>
                <div v-if="errorMessage"
                    class="flex items-center justify-between p-2 mb-4 w-64 text-sm text-red-700 font-semibold border border-red-400 rounded-lg bg-gradient-to-r from-rose-200 to-rose-50">
                    {{ "⚠️ " + errorMessage }}
                    <button @click="clearErrorMessage"
                        class="p-1 w-6 h-6 flex items-center justify-center rounded bg-transparent hover:bg-rose-200">✕</button>
                </div>
                <input v-model="user.name" placeholder="Name"
                    class="mb-4 p-2 w-64 border rounded-lg bg-gray-100 focus:outline-none focus:ring-2 focus:border-blue-500" />
                <input v-model="user.email" placeholder="Email address"
                    class="mb-4 p-2 w-64 border rounded-lg bg-gray-100 focus:outline-none focus:ring-2 focus:border-blue-500" />
                <input v-model="user.password" placeholder="Password" type="password"
                    class="mb-6 p-2 w-64 border rounded-lg bg-gray-100 focus:outline-none focus:ring-2 focus:border-blue-500" />
                <button @click="submit"
                    class="mb-4 w-64 p-2 bg-blue-400 hover:bg-blue-500 text-white rounded-lg shadow-md">Sign up</button>
            </div>
        </div>
    </body>
</template>

<script setup>
import { useRouter } from 'vue-router'
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
    name: '',
    email: '',
    password: ''
})

const errorMessage = ref('')
const infoMessage = ref('')
const router = useRouter()

const submit = async () => {
    if (!user.value.name || !user.value.email || !user.value.password) {
        errorMessage.value = 'Failed to fetch'
        return
    }

    try {
        errorMessage.value = ''
        infoMessage.value = ''
        const data = await $fetch('http://localhost:8000/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: { ...user.value }
            // body: { name: user.value.name, email: user.value.email, password: user.value.password }
        })
        if (data.status === 'success') {
            router.push({
                path: '/SignIn',
            })
        } else if (data.status === 'info') {
            infoMessage.value = data.detail
        }
    } catch (error) {
        console.error('Error:', error)
    }
}

const clearErrorMessage = () => {
    errorMessage.value = ''
}
const clearinfoMessage = () => {
    infoMessage.value = ''
}

</script>