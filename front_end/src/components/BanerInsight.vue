<template>
    <div id="nav">
        <div id="links"> 
            <router-link to="/" id=logo-img>
                <img :src="logo">
            </router-link>
        </div>
        <div id='title'>
            <Title title_page="Criar Insight" />
        </div>
    </div>
</template>

<script>
import Title from './Title.vue'

export default {
    name: 'Navbar',
    props: ['logo'],
    components:{
    Title
  }
}
</script>

<style scoped>
    #nav{
        background-image: url('/img/background.svg');
        width: 414px;
        height: 200px;
        background-repeat: no-repeat;
        display: block;
        
    }

    #nav #links{
        display: flex;
    }

    #title{
        text-align: center;
        font-size: 18pt;
        padding: 0px;
    }
    #nav #logo-img{
        margin: auto;
        margin-left: 0px;
        margin-top: 20px;
    }
</style>
