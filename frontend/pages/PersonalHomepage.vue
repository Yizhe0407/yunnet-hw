// PersonalHomepage.vue
<template>
    <body class="font-mono">
        <div class="flex justify-center items-center h-screen bg-gradient-to-bl from-cyan-50 to-amber-50">
            <div class="p-8 text-center">
                <h1 class="text-2xl font-semibold mb-6">Welcome, {{ name }}!</h1>
                <p class="mb-4 text-lg">Your email: {{ email }}</p>
                <!-- Add more personal homepage content here -->
            </div>
        </div>
    </body>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const name = ref(route.query.name)
const email = ref(route.query.email)
</script>
