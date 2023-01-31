<template> 
    <v-select @search="getEvent" :options="eventsList"
    label="name" @update:modelValue="$emit('update:modelValue',$event)"/>
</template>
<script>
import vSelect from "vue-select"
import axios from 'axios'
export default{
    name:"select-type",
    props:['modelValue'],
    components:{
        vSelect,
    },
    data(){
        return {
            eventName:'',
            eventsList:[],
        }
    },
    mounted(){
        this.getEvent()
    },
    methods:{
        async getEvent(search){
            let   params={name__icontains:search}
            let data =  (await axios.get('/api/event/',{params})).data
            this.eventsList = data.results
        },
    }
}
</script>