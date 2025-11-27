using UnityEngine;

public class ShopManager : MonoBehaviour
{
    [SerializeField]
    public int fuelcost = 2;

    void Awake()
    {
        fuelcost = 2; // 초기 가격 설정
    }

    public void Buyfuel()
    {
        // ScoreManager가 없으면 실행 중지 (안전 장치)
        if (ScoreManager.Instance == null)
        {
            Debug.LogError("ScoreManager가 없습니다! Home 씬에 ScoreManager가 있는지 확인하세요.");
            return;
        }

        int totalScore = ScoreManager.Instance.getTotalScore();

        if (totalScore >= fuelcost)
        {
            // 1. 돈 차감
            totalScore -= fuelcost;
            ScoreManager.Instance.SetTotalScore(totalScore);

            // 2. ScoreManager에 저장된 연료통 영구 업그레이드
            ScoreManager.Instance.UpgradeFuelLimit(10f);

            //Debug.Log("구매 성공! 남은 돈: " + totalScore + ", 현재 연료통 크기: " + ScoreManager.Instance.MaxFuelLimit);
        }
        else
        {
            Debug.Log("골드가 부족합니다. 현재 골드: " + totalScore);
        }
    }
}