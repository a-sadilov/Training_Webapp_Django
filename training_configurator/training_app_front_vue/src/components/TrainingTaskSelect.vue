<template> 
    <v-select @search="getTrainingTask" :options="trainingsList"
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
            trainingName:'',
            trainingsList:[],
        }
    },
    mounted(){
        this.getTrainingTask()
    },
    methods:{
        async getTrainingTask(search){
            let   params={name__icontains:search}
            let data =  (await axios.get('/api/training-task/',{params})).data
            this.trainingsList = data.results
        },
    }
}
</script>