<template>
    <div class="message-container">
        <p> {{ msg }}</p>
    </div>  
</template>

<script>

export default {
    name: "Message",
    props: ['msg']
}

</script>


<style scoped>

.message-container{
    color: #ED4D77;
    background-color: #d697a8;
    padding: 10px;
    border-radius: 8px;
}

</style>