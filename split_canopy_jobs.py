#!/usr/bin/python

from epmt import epmt_query as eq

def main():
    job_type_list=['analysis', 'clean', 'combine', 'data-catalog', 'make-timeavgs','mask-atmos-plevel','pp-starter','regrid-xy','remap-pp-components', 'rename-split-to-pp','split-netcdf','stage-history']
    exp_name='c96L65_am5f5b7r0_pdclim2010F'
    canopy_jobs=eq.get_jobs( fltr=(eq.Job.user_id == 'oar.gfdl.am5'), tags = 'exp_fre_mod:canopy;exp_name:'+exp_name, fmt = 'dict')
    
    
    job_type_ids_dict={}
    for job_type in job_type_list:
        job_type_ids_dict[job_type]=[]
        
    print(job_type_ids_dict)
        
    for job in canopy_jobs:
        jobname=job['jobname']
        for job_type in job_type_list:
            if job_type in jobname:
                job_type_ids_dict[job_type].append(job['jobid'])
                break
    
    print(job_type_ids_dict)    
            
if __name__=='__main__':
    main()
