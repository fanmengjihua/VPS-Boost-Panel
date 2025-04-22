from fastapi import APIRouter
from core import bbr_manager, sysctl_tuner
from utils import speedtest

router = APIRouter()

@router.get("/bbr/status")
def get_bbr_status():
    return {"status": bbr_manager.check_bbr_status()}

@router.post("/bbr/enable")
def enable_bbr():
    bbr_manager.enable_bbr()
    return {"message": "BBR enabled"}

@router.post("/sysctl/optimize")
def optimize_sysctl():
    sysctl_tuner.optimize()
    return {"message": "Sysctl tuned"}

@router.get("/speedtest")
def run_speedtest():
    result = speedtest.run_speedtest()
    return result