using UnityEngine;

public class ScoreManager : MonoBehaviour
{
    public static ScoreManager Instance;

    public int Score { get; private set; }
    public int BestScore { get; private set; }
    public int TotalScore { get; private set; }

    // [핵심] 씬이 바뀌어도 유지되는 연료통 크기 (기본값 30)
    public float MaxFuelLimit = 30f;

    void Awake()
    {
        //Debug.Log("ScoreManager 생성됨: " + gameObject.scene.name);

        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject); // 절대 파괴되지 않음
        }
        else
        {
           // Debug.Log("중복 ScoreManager 삭제됨: " + gameObject.scene.name);
            Destroy(gameObject);
        }
    }

    public void ResetScore()
    {
        Score = 0;
        //Debug.Log("점수 초기화 완료: " + Score);
    }

    public void AddScore(int amount)
    {
        Score += amount;
    }

    // [핵심] 상점에서 호출할 연료 업그레이드 함수
    public void UpgradeFuelLimit(float amount)
    {
        MaxFuelLimit += amount;
    }

    // 기존 getter/setter 유지 (다른 스크립트 호환성 위해)
    public int getScore()
    {
        return Score;
    }
    public int getTotalScore()
    {
        return TotalScore;
    }
    public void SetTotalScore(int scre)
    {
        TotalScore = scre;
    }

    public void SaveScore()
    {
        if (Score > BestScore)
            BestScore = Score;

        TotalScore += Score;
    }
}