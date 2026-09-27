<script setup>
import { onMounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { api } from '../api.js'

const route = useRoute()
const router = useRouter()
const job = ref(null)
const err = ref('')

async function load() {
  err.value = ''
  job.value = null
  try {
    job.value = await api(`/api/jobs/${route.params.id}`)
  } catch (e) {
    err.value = String(e.message || e)
  }
}

onMounted(load)
watch(() => route.params.id, load)
</script>

<template>
  <div>
    <p>
      <button type="button" @click="router.push('/')">返回总览</button>
    </p>
    <p v-if="err" style="color:#b00020">{{ err }}</p>
    <section v-if="job" style="margin:16px 0; padding:12px; border:1px solid #ccc;">
      <h3>任务详情 #{{ job.id }}</h3>
      <p>灯种：{{ job.lamp }}</p>
      <p>标称 nm：{{ job.nominal_nm }}</p>
      <p>实测 nm：{{ job.measured_nm }}</p>
      <p>状态：{{ job.status }}</p>
      <p>
        结论：
        <span
          v-if="job.verdict"
          class="verdict-badge"
          :class="job.verdict === '合格' ? 'pass' : 'fail'"
        >{{ job.verdict }}</span>
      </p>
      <p>理由：{{ job.reason }}</p>
    </section>
  </div>
</template>

<style scoped>
.verdict-badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  color: #fff;
  font-size: 13px;
}
.verdict-badge.pass {
  background: #1e8e3e;
}
.verdict-badge.fail {
  background: #b00020;
}
</style>
