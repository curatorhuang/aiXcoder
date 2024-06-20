<!--红色的标题，居中展示。标题下面是一个按钮，点击按钮，标题数字+1-->
<template>
  <div class="counter">
    <H1>{{count}}</H1>
    <button @click="increment">+1</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    };
  },
  methods: {
    increment() {
      this.count++;
    }
  }
};
</script>

<style>
.counter {
  text-align: center;
}
</style>

