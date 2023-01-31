<template>
    <div class="container">
        <h2> Доска событий </h2> 
        <div class="row">
            <div class="col-md-6 col-lg-3">
                <div class="widget-small primary coloured-icon">
                    <i class="icon fa fa-files-o fa-3x"></i>
                    <div class="info">
                        <h4> Total Completed Events</h4>
                        <p><b> 5 </b></p>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-3">
                <div class="widget-small info coloured-icon">
                    <i class="icon fa fa-thumbs-o-up fa-3x"></i>
                    <div class="info">
                        <h4> Total Running Events </h4>
                        <p><b> 3 </b></p>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-3">
                <div class="widget-small warning coloured-icon">
                    <i class="icon fa fa-users fa-3x"></i>
                    <div class="info">
                        <h4> Total Participants</h4>
                        <p><b> 10 </b></p>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-lg-3">
                <div class="widget-small danger coloured-icon">
                    <i class="icon fa fa-star fa-3x"></i>
                    <div class="info">
                        <h4> Stars </h4>
                        <p><b> 500 </b></p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-2">
                <h2> Фильтры</h2>
                <div>
                Название
                </div>
                <event-select v-model="filters.event"/>

                <div>
                Название
                </div>
                <input v-model="filters.name__icontains" class="form-control"/>

                <div>
                Упражнения
                </div>
                <task-select v-model="filters.task"/>

            </div>
        </div>
        <div class="col-10">
            <div class="tile">
                <div class="tile-body">
                    <div class="table-responsive">
                        <div id="sampleTable_wrapper" class="dataTables_wrapper container-fluid dt-bootstrap4 no-footer">
                            <div class="row">
                                <div class="col-sm-12">
                                    <table class="table table-hover table-bordered dataTable no-footer" id="sampleTable" role="grid" aria-describedby="sampleTable_info">
                                        <thead>
                                            <tr role="row">
                                                <th class="sorting_asc" tabindex="0" aria-controls="sampleTable" rowspan="1" colspan="1" aria-sort="ascending" aria-label="Name: activate to sort column descending" style="width: 261.641px;">SL</th>
                                                <th class="sorting" tabindex="0" aria-controls="sampleTable" rowspan="1" colspan="1" aria-label="Position: activate to sort column ascending" style="width: 417.312px;"> Название события</th>
                                                <th class="sorting" tabindex="0" aria-controls="sampleTable" rowspan="1" colspan="1" aria-label="Office: activate to sort column ascending" style="width: 189.281px;"> Начало</th>
                                                <th class="sorting" tabindex="0" aria-controls="sampleTable" rowspan="1" colspan="1" aria-label="Age: activate to sort column ascending" style="width: 102.141px;"> Конец </th>
                                                <th class="sorting" tabindex="0" aria-controls="sampleTable" rowspan="1" colspan="1" aria-label="Age: activate to sort column ascending" style="width: 102.141px;"> Группы мышц </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(event,idx) in eventsList" :key="event.id" @click="toDetail(event)">
                                                <td>{{event.id}}</td>
                                                <td>{{event.name}}</td>
                                                <td>
                                                    <div v-for="task in event.tasks" :key="task.name">{{task.name}}</div>
                                                </td>
                                                <td> {{event.start_time}}</td>
                                                <td> {{event.end_time}}</td>
                                                <td @click.stop="toTask(event.tasks)">{{art.tasks? art.tasks.name:''}}</td>
                                                <td> <button @click="deleteEvent(event,idx)"> Удалить  </button></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <nav aria-label="Page navigation example">
            <ul class="pagination">
                <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                <li class="page-item" :class="activePage==x? 'active':''" v-for="x in maxPage" :key="x" @click="selectPage(x)"><a class="page-link" href="#">{{x}}</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
            </ul>
        </nav>
    </div>

</template>
<script>

//import axios from 'axios'
import EventSelect from "@/components/EventSelect"
import TaskSelect  from "@/components/TaskSelect"
import {Event} from "@/api.js"
export default{
    name:'dashboard-view',
   data(){
        return {
            filters:{},
            searchFiedl:'',
            EventSelect:{},
            maxPage:1,
            activePage:1,
            eventsList:[
            ]
        }
    },
    components:{
        EventSelect,
        TaskSelect,
    },
    watch:{
        searchFiedl(){
            this.getEvent()
        },
        filters:{
            deep:true,
            handler(){
                this.getEvent()
            },
        },
    },
    mounted(){
        this.getEvent()
    },
    methods:{
        selectPage(p){
            this.activePage=p
            this.getEvent()
        },
        toTask(task){
            this.$router.push({name:'task-detail',params:{id:task.id}})
        },
        toDetail(event){
            this.$router.push({name:'event-detail',params:{id:event.id}})
        },
        async deleteEvent(art,idx){
            await Event.objects.delete(art)
            this.eventsList.splice(idx,1)
        },
        setOrdering(filed_name){
            this.filters.ordering = this.filters.ordering==filed_name? '-'+filed_name: filed_name
        },
        updateAutho(event){
            this.filters['author']=event.id
        },
        async getEvent(){
            //let params = {
            //    author__name__icontains:this.searchFiedl,
            //    author:this.selectAuthor.id
            //}
            let params = {...this.filters,page:this.activePage}
            params['tasks'] = this.filters.tasks? this.filters.tasks.id:undefined
            //  params['author'] = this.filters.author? this.filters.author.id:undefined
            let response = await Event.objects.filter(params)
            this.maxPage = response.total_pages
            //let data =  (await axios.get('/api/article/',{params})).data
            this.eventsList = response.results
        }
    },
}
</script>