<template> 
    <v-select @search="getTask" :options="tasksList"
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
            taskName:'',
            tasksList:[],
        }
    },
    mounted(){
        this.getTask()
    },
    methods:{
        async getTask(search){
            let   params={name__icontains:search}
            let data =  (await axios.get('/api/task/',{params})).data
            this.tasksList = data.results
        },
    }
}
</script>